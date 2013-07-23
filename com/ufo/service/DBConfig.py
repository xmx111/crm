#-*-coding:utf-8-*-
host = '192.168.1.221:3316'
user = 'root'
password = 'csany'
db = 'crm'
charset = 'utf-8'
mysqlstr = 'mysql://%s:%s@%s/%s?charset=%s'%(user,password,host,db,charset)
sqlitestr = 'sqlite:///test.db'