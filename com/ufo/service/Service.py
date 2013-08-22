#-*-coding:utf-8-*-
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
import sys
import os
import DBConfig
from datetime import datetime, date
from utils.EncryptUtils import Encrypt
reload(sys)
sys.setdefaultencoding('utf-8')

engine = create_engine(DBConfig.mysqlstr, echo=False)
#engine = create_engine(DBConfig.sqlitestr, echo=True)
# 定义一个函数，用来获取sqlalchemy的session
def bindSQL():
    return scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

class Page():
    index = 1 # 当前页
    pageRows = 15 # 每页行数
    totalRows = 0 # 总行数
    url = '#' # 链接
    parms = '' # 参数
    PAGE_POSITION_OFFSET = 7 # 分页的位置序号同实际数据页序号的偏移位置
    PAGE_POSTION_COUNT = 5 # 分页的跳转选择显示页数
    def __init__(self, index = 1, totalRows = 0, url = '#', parms = '', pageRows = 15):
        self.index = index
        self.totalRows = totalRows
        self.url = url
        self.parms = parms
        self.pageRows = pageRows
    def getBeforePage(self):
        rows = self.getPageCount()
        before = self.index + self.PAGE_POSTION_COUNT - rows if self.index + self.PAGE_POSTION_COUNT > rows else 0
        if before == 0:
            before = self.index - self.PAGE_POSTION_COUNT if self.index - self.PAGE_POSTION_COUNT > 0 else 1
        else:
            before = 1 if self.index - before - self.PAGE_POSTION_COUNT < 1 else self.index - before - self.PAGE_POSTION_COUNT
        return before
    def getAfterPage(self):
        rows = self.getPageCount()
        after = self.PAGE_POSTION_COUNT - self.index if self.index - self.PAGE_POSTION_COUNT < 1 else 0
        if after == 0:
            after = rows if self.index + self.PAGE_POSTION_COUNT > rows else self.index + self.PAGE_POSTION_COUNT
        else:
            after = rows if self.index + after + self.PAGE_POSTION_COUNT + 1 > rows else self.index + after + self.PAGE_POSTION_COUNT + 1
        return after
    def getPageCount(self):
        if self.pageRows == 0:
            return 0
        if self.totalRows == 0:
            return 0
        else:
            i = self.totalRows / self.pageRows + 1 if self.totalRows % self.pageRows != 0 else self.totalRows / self.pageRows
            i = i if i != 0 else 1
            return i
    def getFuncScrpit(self):
        if self.totalRows == 0:
            return ''
        beforePage = self.getBeforePage()
        afterPage = self.getAfterPage()
        script = '<ul>'
        if self.index != 1:
            script += '<li><a href="' + self.getFuncUrl(self.index - 1) + '">前页</a></li>'
        else:
            script += '<li class="disabled"><a href="#">前页</a></li>'
        for i in range(beforePage, afterPage + 1):
            if beforePage == 0:
                script += '<li class="active"><a href="#">1</a></li>'
                break
            if i == self.index:
                script += '<li class="active"><a href="#">' + str(i) + '</a></li>'
                continue
            script += '<li><a href="' + self.getFuncUrl(i)  + '">' + str(i) + '</a></li>'
        if self.index != self.getPageCount():
            script += '<li><a href="' + self.getFuncUrl(self.index + 1)  + '">后页</a></li>'
        else:
            script += '<li class="disabled"><a href="#">后页</a></li>'
        return script
    def getFuncUrl(self, pageIndex):
        return 'javascript:fillDivContGET(\'' + self.url + '?page=' + str(pageIndex) + self.parms + '\', \'changeDiv\')'

class User(Base):
    __tablename__ = "rainbow_user"
    userId = Column(Integer, primary_key=True)
    userName = Column(String(45), unique=True)
    password = Column(String(45))
    name = Column(String(45), unique=True)
    secName = Column(String(45))
    cardid = Column(String(45), unique=True)
    email = Column(String(45), unique=True)
    sex = Column(Integer)
    birsday = Column(Date)

    customs = relationship("Custom")
    def __init__(self, userName='', password='', name=''):
        self.userName = userName
        self.password = Encrypt.md5(password)
        self.name = name

    @staticmethod
    def add(user):
        session=bindSQL()
        session.add(user)
        session.commit()

    @staticmethod
    def editPwd(userId, password):
        session=bindSQL()
        user = session.query(User).filter(User.userId==userId).first()
        user.password = Encrypt.md5(password)
        session.commit()

    @staticmethod
    def getUserByUserName(userName):
        session=bindSQL()
        user = session.query(User).filter(User.userName==userName).first() 
        return user

    @staticmethod
    def editUserInfo(userId, name, cardid, sex, birsday):
        session=bindSQL()
        user = session.query(User).filter(User.userId==userId).first()
        user.name = name
        user.cardid = cardid
        user.sex = sex
        user.birsday = birsday
        session.commit()

class Custom(Base):
    __tablename__ = "rainbow_custom"
    customId = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey("rainbow_user.userId"))
    customType = Column(Integer)
    name = Column(String(45))
    phone = Column(String(45), unique=True)
    cardid = Column(String(45), unique=True)
    sex = Column(Integer)
    marriage = Column(Integer)
    addr = Column(String(200))
    regAddr = Column(String(200))
    creditCardInfo = Column(String(200))
    linkmanInfo = Column(String(400))
    houseAddr = Column(String(200))
    company = Column(String(200))
    companyTel = Column(String(15))
    companyAttr = Column(String(200))
    companyDate = Column(Date)
    salary = Column(Float)
    consultTime = Column(Date)
    creditDate = Column(Date)
    repayDate = Column(Date)
    creditMoney = Column(Float)
    creditInterest = Column(Float)
    creditTerm = Column(Integer)
    enterTime = Column(Date)
    applyCompany = Column(String(400))
    creditCompany = Column(String(400))
    saveTime = Column(DateTime, default=datetime.now)
    notPassReazon = Column(String(400))

    customFiles = relationship("CustomFile")
    def __init__(self, userId, customType=0, name=''):
        self.userId = userId
        self.customType = customType
        self.name = name

    @staticmethod
    def add(custom):
        session=bindSQL()
        session.add(custom)
        session.commit()
        return custom.customId

    @staticmethod
    def addAndFile(custom, fileValue):
        session=bindSQL()
        session.flush()
        if fileValue != '':
            for str in fileValue.split(','):
                if str != '':
                    cFile = CustomFile(str.split('@')[0], str.split('@')[1])
                    custom.customFiles.append(cFile)

        session.add(custom)
        session.commit()
        for cFile2 in custom.customFiles:
            if os.path.exists(os.path.join("static", "tmp", cFile2.filePathName)):
                os.rename(os.path.join("static", "tmp", cFile2.filePathName), os.path.join("static", "custom", cFile2.filePathName))
        return custom.customId

    @staticmethod
    def editAndFile(custom, fileValue, rmFileValue):
        session=bindSQL()
        customQuery = session.query(Custom).filter(Custom.customId==custom.customId).first()
        if custom.phone != None and custom.phone != customQuery.phone and Custom.getCustomByPhone(custom.phone) != None:
            return "2"
        if custom.cardid != None and custom.cardid != customQuery.cardid and Custom.getCustomByCardid(custom.cardid) != None:
            return "3"
        customQuery.customType = custom.customType
        customQuery.name = custom.name
        customQuery.phone = custom.phone
        customQuery.cardid = custom.cardid
        customQuery.sex = custom.sex
        customQuery.marriage = custom.marriage
        customQuery.addr = custom.addr
        customQuery.regAddr = custom.regAddr
        customQuery.creditCardInfo = custom.creditCardInfo
        customQuery.linkmanInfo = custom.linkmanInfo
        customQuery.houseAddr = custom.houseAddr
        customQuery.company = custom.company
        customQuery.companyTel = custom.companyTel
        customQuery.companyAttr = custom.companyAttr
        customQuery.companyDate = custom.companyDate
        customQuery.salary = custom.salary
        customQuery.consultTime = custom.consultTime
        customQuery.creditDate = custom.creditDate
        customQuery.repayDate = custom.repayDate
        customQuery.creditMoney = custom.creditMoney
        customQuery.creditInterest = custom.creditInterest
        customQuery.creditTerm = custom.creditTerm
        customQuery.enterTime = custom.enterTime
        customQuery.applyCompany = custom.applyCompany
        customQuery.creditCompany = custom.creditCompany

        # 添加的文件名
        fileDict = {x.split('@')[1] : x.split('@')[0]  for x in fileValue.split(',') if x!=''} if fileValue != '' else {}
        # 删除的文件名
        rmFileList = [x.split('@')[1] for x in rmFileValue.split(',') if x!=''] if rmFileValue != '' else []

        rmCustomFiles = [customFile for customFile in customQuery.customFiles if customFile.filePathName in rmFileList]
        for rmFile in rmCustomFiles:
            session.delete(rmFile)
        
        customQuery.customFiles = [customFile for customFile in customQuery.customFiles if customFile.filePathName not in rmFileList]

        for filePathName in fileDict.keys():
            cFile = CustomFile(fileDict[filePathName], filePathName)
            customQuery.customFiles.append(cFile)
        # 添加文件
        for filePathName in fileDict.keys():
            if os.path.exists(os.path.join("static", "tmp", filePathName)):
                os.rename(os.path.join("static", "tmp", filePathName), os.path.join("static", "custom", filePathName))
        # 删除文件
        for rmName in rmFileList:
            if os.path.exists(os.path.join("static", "custom", rmName)):
                os.remove(os.path.join("static", "custom", rmName))
        session.commit()
        return "1"

    @staticmethod
    def queryCustom(page, customType, name, phone, cardid):
        session=bindSQL()
        query = session.query(Custom)
        if customType != None:
            query = query.filter(Custom.customType==customType)
        if name != None:
            query = query.filter(Custom.name.like('%' + name + '%'))
        if phone != None:
            query = query.filter(Custom.phone.like('%' + phone + '%'))
        if cardid != None:
            query = query.filter(Custom.cardid.like('%' + cardid + '%'))
        pageObj = Page(page, query.count())
        customs = query[(pageObj.index - 1) * pageObj.pageRows : pageObj.index * pageObj.pageRows]
        return customs, pageObj

    @staticmethod
    def getCustomById(customId):
        session=bindSQL()
        custom = session.query(Custom).filter(Custom.customId==customId).first()
        return custom
    @staticmethod
    def getCustomByPhone(phone):
        session=bindSQL()
        custom = session.query(Custom).filter(Custom.phone==phone).first()
        return custom
    @staticmethod
    def getCustomByCardid(cardid):
        session=bindSQL()
        custom = session.query(Custom).filter(Custom.cardid==cardid).first()
        return custom
    @staticmethod
    def delete(customId):
        session=bindSQL()
        custom = session.query(Custom).filter(Custom.customId==customId).first()
        for customFile in custom.customFiles:
            session.delete(customFile)
        session.delete(custom)
        session.commit()

class CustomFile(Base):
    __tablename__ = "rainbow_custom_file"
    fileId = Column(Integer, primary_key=True)
    customId = Column(Integer, ForeignKey("rainbow_custom.customId"))
    fileType = Column(Integer, default=0)
    fileName = Column(String(200))
    filePathName = Column(String(200))
    saveTime = Column(DateTime, default=datetime.now)
    def __init__(self, fileName='', filePathName='', fileType=0):
        self.fileType = fileType
        self.fileName = fileName
        self.filePathName = filePathName
    @staticmethod
    def add(customFile):
        session=bindSQL()
        session.add(customFile)
        session.commit()

metadata = Base.metadata

if __name__ == '__main__':
    metadata.create_all(engine)
    user = User(u'李彩娟', '111111', u'李彩娟')
    user.sex = 1
    user.birsday = date(1986,10,8)
    session=bindSQL()
    session.add(user)
    session.commit()