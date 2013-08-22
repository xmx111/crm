#-*-coding:utf-8-*-
host = '192.168.1.221:3316'
#host = '127.0.0.1:3306'
user = 'root'
password = 'csany'
#password = 'root'
db = 'crm2'
charset = 'utf8'
mysqlstr = 'mysql://%s:%s@%s/%s?charset=%s'%(user,password,host,db,charset)
sqlitestr = 'sqlite:///lcjdb.db'