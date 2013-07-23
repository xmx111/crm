#-*-coding:utf-8-*-
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import DBConfig

#engine = create_engine('mysql://%s:%s@%s/%s?charset=%s'%(DBConfig.user,DBConfig.password,DBConfig.host,DBConfig.db,DBConfig.charset), echo=True)
engine = create_engine(DBConfig.sqlitestr, echo=True)
# 定义一个函数，用来获取sqlalchemy的session
def bindSQL():
    return scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

class User(Base):
    __tablename__ = "rainbow_user"
    id = Column(Integer, primary_key=True)
    username = Column(String(45), unique=True)
    password = Column(String(45), unique=True)
    name = Column(String(45), unique=True)
    secname = Column(String(45), unique=True)
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
    user = User(u'李彩娟', '111111', 'lcj')
    session=bindSQL()
    session.add(user)
    session.commit()