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



metadata = Base.metadata

if __name__ == '__main__':
    metadata.create_all(engine)
    custom = Custom(1, 0, '客户')
    session=bindSQL()
    session.add(custom)
    session.commit()