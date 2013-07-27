#-*-coding:utf-8-*-
host = '127.0.0.1:3306'
user = 'root'
password = ''
db = 'crm'
charset = 'utf8'
mysqlstr = 'mysql://%s:%s@%s/%s?charset=%s'%(user,password,host,db,charset)
sqlitestr = 'sqlite:///test.db'