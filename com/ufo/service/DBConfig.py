#-*-coding:utf-8-*-
# bae3.0 bae.core.const已被删除
'''
from bae.core import const
host = const.MYSQL_HOST
port = const.MYSQL_PORT
user = const.MYSQL_USER
password = const.MYSQL_PASS
'''
api_key = "xxxxxxxxxx" # 百度云存储的api key
secret_key = "xxxxxxxxxx" # 百度云存储的secret key
host = "sqld.duapp.com"
port = 4050
user = api_key
password = secret_key
db = 'jmpCeURFiSAATDOLKwjG'
charset = 'utf8'
mysqlstr = 'mysql://%s:%s@%s:%s/%s?charset=%s'%(user,password,host,port,db,charset)
sqlitestr = 'sqlite:///lcjdb.db'