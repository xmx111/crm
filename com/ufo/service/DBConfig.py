#-*-coding:utf-8-*-
from bae.core import const
host = const.MYSQL_HOST
port = const.MYSQL_PORT
user = const.MYSQL_USER
password = const.MYSQL_PASS
db = 'jmpCeURFiSAATDOLKwjG'
charset = 'utf8'
mysqlstr = 'mysql://%s:%s@%s:%s/%s?charset=%s'%(user,password,host,port,db,charset)
sqlitestr = 'sqlite:///lcjdb.db'