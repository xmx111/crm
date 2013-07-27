#-*-coding:utf-8-*-
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import sys
import DBConfig
reload(sys)
sys.setdefaultencoding('utf-8')

engine = create_engine(DBConfig.mysqlstr, echo=True)
#engine = create_engine(DBConfig.sqlitestr, echo=True)
# 定义一个函数，用来获取sqlalchemy的session
def bindSQL():
    return scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

class User(Base):
    __tablename__ = "rainbow_user"
    id = Column(Integer, primary_key=True)
    username = Column(String(45), unique=True)
    password = Column(String(45))
    name = Column(String(45), unique=True)
    secname = Column(String(45))
    cardid = Column(String(45), unique=True)
    def __init__(self, username='', password='', name='', secname='', cardid=''):
        self.name = name
        self.username = username
        self.password = password
        self.secname = secname
        self.cardid = cardid

metadata = Base.metadata

if __name__ == '__main__':
    metadata.create_all(engine)
<<<<<<< HEAD
    user = User('lcj1', '111111', 'lcj')
=======
    user = User('李彩娟', '111111', 'lcj')
>>>>>>> 8651dce56066c06359b339d21366301521e581bc
    session=bindSQL()
    session.add(user)
    session.commit()