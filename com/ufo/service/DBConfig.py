#-*-coding:utf-8-*-
# bae3.0 bae.core.constÒÑ±»É¾³ý
'''
from bae.core import const
host = const.MYSQL_HOST
port = const.MYSQL_PORT
user = const.MYSQL_USER
password = const.MYSQL_PASS
'''
api_key = "X1p8KwhrRfpv3rMP9bej3hqj"
secret_key = "OkV35Zq1OyXNSFVB3MdrUGgxmcTbGGk5"
host = "sqld.duapp.com"
port = 4050
user = api_key
password = secret_key
db = 'jmpCeURFiSAATDOLKwjG'
charset = 'utf8'
mysqlstr = 'mysql://%s:%s@%s:%s/%s?charset=%s'%(user,password,host,port,db,charset)
sqlitestr = 'sqlite:///lcjdb.db'