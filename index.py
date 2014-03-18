#-*-coding:utf-8-*-
import web
import sys, os
import uuid
import re
from datetime import datetime
from com.ufo.service.Service import User, Custom, CustomFile, FileValue
from com.ufo.service.utils.EncryptUtils import Encrypt
from com.ufo.service.utils.YunPanUtils import baidu
import logging
# BAE3.0 bae.core.const已被删除，已经有了可以直接使用/tmp/的权限
#from bae.core import const
#import tempfile

# web.py中file使用的系统默认的/tmp/xxx目录，由于BAE2.0上面修改了tempfile，所以修改tempfile路径
# BAE3.0 bae.core.const已被删除，已经有了可以直接使用/tmp/的权限
#tempfile.tempdir = const.APP_TMPDIR
#import cStringIO 
#def TemporaryFile(mode='w+b', bufsize=-1, suffix="", prefix='', dir=None): 
#    return cStringIO.StringIO() 
#tempfile.TemporaryFile = TemporaryFile

reload(sys)
sys.setdefaultencoding('utf-8')

web.config.debug = False

urls = (
    '/', 'index',
    '/login','login', 
    '/logout', 'logout',

    '/userView', 'userView',
    '/user', 'user',
    '/pwd', 'pwd',

    '/customView', 'customView',
    '/customEditView', 'customEditView',
    '/custom', 'custom',
    '/customList', 'customList',
    '/customUpload', 'customUpload',
    '/customCheckPhone/(.+)', 'customCheckPhone',
    '/customCheckCardid/(.+)', 'customCheckCardid',
    
    '/test', 'test',
    )

app_root = os.path.dirname(__file__)

app = web.application(urls, globals())

web.config.session_parameters['cookie_name'] = 'webpy_session_id'
web.config.session_parameters['cookie_domain'] = None
web.config.session_parameters['timeout'] = 1800, #24 * 60 * 60, # 24 hours   in seconds
web.config.session_parameters['ignore_expiry'] = True
web.config.session_parameters['ignore_change_ip'] = True
web.config.session_parameters['secret_key'] = 'lkjsdIfnnM97fwoP'
web.config.session_parameters['expired_message'] = 'Session expired'

# bae2.0 没有/tmp/的权限使用指定目录const.APP_TMPDIR
#session = web.session.Session(app, web.session.DiskStore(os.path.join(const.APP_TMPDIR,'sessions')),)
# bae3.0 bae.core.const已被删除，已经有了可以直接使用/tmp/的权限
session = web.session.Session(app, web.session.DiskStore('sessions'),)

templates_root = os.path.join(app_root, 'template')
render = web.template.render(templates_root)
renderUser = web.template.render(os.path.join(app_root, 'template', 'user'))
renderCustom = web.template.render(os.path.join(app_root, 'template', 'custom'))

# 取数模板（比如查看客户信息）不要用GET，IE会缓存，修改后页面不变
# 系统模块
class index:
    def GET(self):
        #传值
        if session.get('user') == None:
            return render.index('', '')
        else:
            return render.main(session.get('user').userName)
        
class login:
    def GET(self):
        return 'login'
    def POST(self):
        data = web.input()

        user = User.getUserByUserName(data['userName'])
        
        if data['userName'] == user.userName and Encrypt.md5(data['password']) == user.password:
            retStr = '登录成功'
            session.user = user
            return render.main(data['userName'])
        else:
            retStr = '用户名或密码错误'
            return render.index('', retStr)
class logout:
    def GET(self):
        session.kill()
        return render.index('', '')

# 用户模块
class userView:
    def POST(self):
        return renderUser.userView(session.user)
class user:
    def GET(self, randomStr):
        return renderUser.userView(session.user)
    def POST(self):
        data = web.input()
        name = data['name'] if data.has_key('name') else None
        cardid = data['cardid'] if data.has_key('cardid') else None
        sex = data['sex'] if data.has_key('sex') else 0
        birsday = data['birsday'] if data.has_key('birsday') else None

        User.editUserInfo(session.get('user').userId, name, cardid, sex, birsday)
        session.user = User.getUserByUserName(session.get('user').userName)
        return '1'
class pwd:
    def GET(self):
        return renderUser.pwdView()
    def POST(self):
        data = web.input()
        if Encrypt.md5(data['oldpassword']) == session.get('user').password:
            User.editPwd(session.get('user').userId, data['password'])
            session.user = User.getUserByUserName(session.get('user').userName)
        else:
            return '0'
        return '1'

# 客户模块
class customView:
    def GET(self):
        return renderCustom.addCustom()
    def POST(self):
        data = web.input()
        customId = data['customId'] if data.has_key('customId') and data['customId'] != 0 else 0
        return renderCustom.viewCustom(Custom.getCustomById(customId))
class customEditView:
    def POST(self):
        data = web.input()
        customId = data['customId'] if data.has_key('customId') and data['customId'] != 0 else 0
        return renderCustom.editCustom(Custom.getCustomById(customId))
class custom:
    def PUT(self):
        data = web.input()
        custom = Custom(session.user.userId, data['customType'])
        custom.customType = data['customType']
        custom.name = data['name']
        custom.phone = data['phone'] if data.has_key('phone') and data['phone'] != '' else None

        if custom.phone != None and Custom.getCustomByPhone(custom.phone) != None:
            return "2"

        custom.cardid = data['cardid'] if data.has_key('cardid') and data['cardid'] != '' else None

        if custom.cardid != None and Custom.getCustomByCardid(custom.cardid) != None:
            return "3"

        custom.sex = data['sex'] if data.has_key('sex') and data['sex'] != '' else 0
        custom.marriage = data['marriage'] if data.has_key('marriage') and data['marriage'] != '' else 0
        custom.addr = data['addr'] if data.has_key('addr') and data['addr'] != '' else None
        custom.regAddr = data['regAddr'] if data.has_key('regAddr') and data['regAddr'] != '' else None
        custom.creditCardInfo = data['creditCardInfo'] if data.has_key('creditCardInfo') and data['creditCardInfo'] != '' else None
        custom.linkmanInfo = data['linkmanInfo'] if data.has_key('linkmanInfo') and data['linkmanInfo'] != '' else None
        custom.houseAddr = data['houseAddr'] if data.has_key('houseAddr') and data['houseAddr'] != '' else None
        custom.company = data['company'] if data.has_key('company') and data['company'] != '' else None
        custom.companyTel = data['companyTel'] if data.has_key('companyTel') and data['companyTel'] != '' else None
        custom.companyAttr = data['companyAttr'] if data.has_key('companyAttr') and data['companyAttr'] != '' else None
        try:
            custom.companyDate = datetime.strptime(data['companyDate'], '%Y-%m-%d') if data.has_key('companyDate') and data['companyDate'] != '' else None
        except:
            return '11'
        custom.salary = data['salary'] if data.has_key('salary') and data['salary'] != '' else None
        try:
            custom.consultTime = datetime.strptime(data['consultTime'], '%Y-%m-%d') if data.has_key('consultTime') and data['consultTime'] != '' else None
        except:
            return '12'
        try:
            custom.creditDate = datetime.strptime(data['creditDate'], '%Y-%m-%d') if data.has_key('creditDate') and data['creditDate'] != '' else None
        except:
            return '13'
        try:
            custom.repayDate = datetime.strptime(data['repayDate'], '%Y-%m-%d') if data.has_key('repayDate') and data['repayDate'] != '' else None
        except:
            return '14'
        custom.creditMoney = data['creditMoney'] if data.has_key('creditMoney') and data['creditMoney'] != '' else None
        custom.creditInterest = data['creditInterest'] if data.has_key('creditInterest') and data['creditInterest'] != '' else None
        custom.creditTerm = data['creditTerm'] if data.has_key('creditTerm') and data['creditTerm'] != '' else None
        try:
            custom.enterTime = datetime.strptime(data['enterTime'], '%Y-%m-%d') if data.has_key('enterTime') and data['enterTime'] != '' else None
        except:
            return '15'
        custom.applyCompany = data['applyCompany'] if data.has_key('applyCompany') and data['applyCompany'] != '' else None
        custom.creditCompany = data['creditCompany'] if data.has_key('creditCompany') and data['creditCompany'] != '' else None
        custom.notPassReazon = data['notPassReazon'] if data.has_key('notPassReazon') and data['notPassReazon'] != '' else None
        '''
        regex = re.compile('^[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}$')
        print type(custom.companyDate)
        if custom.companyDate is not None and re.match(regex, custom.companyDate) is None:
            return '11'
        if custom.consultTime is not None and re.match(regex, custom.consultTime) is None:
            return '12'
        if custom.creditDate is not None and re.match(regex, custom.creditDate) is None:
            return '13'
        if custom.repayDate is not None and re.match(regex, custom.repayDate) is None:
            return '14'
        if custom.enterTime is not None and re.match(regex, custom.enterTime) is None:
            return '15'
        '''
        fileValue = data['fileValue'] if data.has_key('fileValue') and data['fileValue'] != '' else ''
        print 'fileValue' + fileValue
        Custom.addAndFile(custom, fileValue)
        return '1'
    def POST(self):
        data = web.input()
        customId = data['customId'] if data.has_key('customId') and data['customId'] != 0 else 0
        if customId == 0:
            return "0"

        custom = Custom(session.user.userId, data['customType'])
        custom.customId = customId
        custom.customType = data['customType']
        custom.name = data['name']
        custom.phone = data['phone'] if data.has_key('phone') and data['phone'] != '' else None
        custom.cardid = data['cardid'] if data.has_key('cardid') and data['cardid'] != '' else None
        custom.sex = data['sex'] if data.has_key('sex') and data['sex'] != '' else 0
        custom.marriage = data['marriage'] if data.has_key('marriage') and data['marriage'] != '' else 0
        custom.addr = data['addr'] if data.has_key('addr') and data['addr'] != '' else None
        custom.regAddr = data['regAddr'] if data.has_key('regAddr') and data['regAddr'] != '' else None
        custom.creditCardInfo = data['creditCardInfo'] if data.has_key('creditCardInfo') and data['creditCardInfo'] != '' else None
        custom.linkmanInfo = data['linkmanInfo'] if data.has_key('linkmanInfo') and data['linkmanInfo'] != '' else None
        custom.houseAddr = data['houseAddr'] if data.has_key('houseAddr') and data['houseAddr'] != '' else None
        custom.company = data['company'] if data.has_key('company') and data['company'] != '' else None
        custom.companyTel = data['companyTel'] if data.has_key('companyTel') and data['companyTel'] != '' else None
        custom.companyAttr = data['companyAttr'] if data.has_key('companyAttr') and data['companyAttr'] != '' else None
        try:
            custom.companyDate = datetime.strptime(data['companyDate'], '%Y-%m-%d') if data.has_key('companyDate') and data['companyDate'] != '' else None
        except:
            return '11'
        custom.salary = data['salary'] if data.has_key('salary') and data['salary'] != '' else None
        try:
            custom.consultTime = datetime.strptime(data['consultTime'], '%Y-%m-%d') if data.has_key('consultTime') and data['consultTime'] != '' else None
        except:
            return '12'
        try:
            custom.creditDate = datetime.strptime(data['creditDate'], '%Y-%m-%d') if data.has_key('creditDate') and data['creditDate'] != '' else None
        except:
            return '13'
        try:
            custom.repayDate = datetime.strptime(data['repayDate'], '%Y-%m-%d') if data.has_key('repayDate') and data['repayDate'] != '' else None
        except:
            return '14'
        custom.creditMoney = data['creditMoney'] if data.has_key('creditMoney') and data['creditMoney'] != '' else None
        custom.creditInterest = data['creditInterest'] if data.has_key('creditInterest') and data['creditInterest'] != '' else None
        custom.creditTerm = data['creditTerm'] if data.has_key('creditTerm') and data['creditTerm'] != '' else None
        try:
            custom.enterTime = datetime.strptime(data['enterTime'], '%Y-%m-%d') if data.has_key('enterTime') and data['enterTime'] != '' else None
        except:
            return '15'
        custom.applyCompany = data['applyCompany'] if data.has_key('applyCompany') and data['applyCompany'] != '' else None
        custom.creditCompany = data['creditCompany'] if data.has_key('creditCompany') and data['creditCompany'] != '' else None
        custom.notPassReazon = data['notPassReazon'] if data.has_key('notPassReazon') and data['notPassReazon'] != '' else None
        '''
        regex = re.compile('^[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}$')
        print type(custom.companyDate)
        if custom.companyDate is not None and re.match(regex, custom.companyDate) is None:
            return '11'
        if custom.consultTime is not None and re.match(regex, custom.consultTime) is None:
            return '12'
        if custom.creditDate is not None and re.match(regex, custom.creditDate) is None:
            return '13'
        if custom.repayDate is not None and re.match(regex, custom.repayDate) is None:
            return '14'
        if custom.enterTime is not None and re.match(regex, custom.enterTime) is None:
            return '15'
        '''

        fileValue = data['fileValue'] if data.has_key('fileValue') and data['fileValue'] != '' else ''
        rmFileValue = data['rmFileValue'] if data.has_key('rmFileValue') and data['rmFileValue'] != '' else ''
        return Custom.editAndFile(custom, fileValue, rmFileValue)
    def DELETE(self):
        data = web.input()
        customId = data['customId'] if data.has_key('customId') and data['customId'] != '' else None
        if customId == None:
            return "0"
        Custom.delete(customId)
        return '1'
class customList:
    def GET(self):
        data = web.input()
        page = int(data['page']) if data.has_key('page') and data['page'] != '' else 1
        customType = int(data['customType']) if data.has_key('customType') and data['customType'] != '-1' else None
        name = data['name'] if data.has_key('name') and data['name'] != '' else None
        phone = data['phone'] if data.has_key('phone') and data['phone'] != '' else None
        cardid = data['cardid'] if data.has_key('cardid') and data['cardid'] != '' else None
        customs, pageObj = Custom.queryCustom(page, customType, name, phone, cardid)
        pageObj.url = '/customList'
        return renderCustom.listCustom(customs, pageObj, customType, name, phone, cardid)
class customUpload:
    def DELETE(self):
        data = web.input()
        fileName = data['fileName'] if data.has_key('fileName') and data['fileName'] != '' else None
        if fileName == None:
            return "0"
        logging.debug('/tmp/' + fileName)
        baidu.delFile('/tmp/' + fileName)
        return "1"
    def POST(self):
        #data = web.input(imgFile={})
        #由于BAE修改了python一些库的代码，上传二进制图片会丢失字节，改为
        data = web.data()
        try:
            # 取文件内容
            import StringIO
            s1 = StringIO.StringIO(data)
            lines = s1.readlines()
            # 第3行为文件名
            fileName = lines[3:4][0].replace('\r\n', '')
            # 去掉15行的协议头和其它一些乱七八糟的东西
            fileValue = ''.join(lines[16:-5]).replace('\\r\\n', '')
            
            s1.close()
            newname = str(uuid.uuid1()) + os.path.splitext(fileName)[1]
            baidu.upload(newname, fileValue, '/tmp/')
        except:
            logging.debug('debug 上传出错:' + str(sys.exc_info()[0]))
            raise
        finally:
            pass
            #if f != None:f.close
        return newname
class customCheckPhone:
    def GET(self, phone):
        if Custom.getCustomByPhone(phone) == None:
            return "0"
        else:
            return "1"
class customCheckCardid:
    def GET(self, cardid):
        if Custom.getCustomByCardid(cardid) == None:
            return "0"
        else:
            return "1"
class test:
    def GET(self):
        return baidu.getFiles()

if __name__ == '__main__':app.run()

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app.wsgifunc())