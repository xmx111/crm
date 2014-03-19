#-*-coding:utf-8-*-
import time
import os
# BAE3.0 bae.core.const已被删除
#from bae.core import const
# bcs
import logging
import pybcs

#设置日志级别
pybcs.init_logging(logging.INFO)

HOST = 'http://bcs.duapp.com/'
AK = 'xxxxxxxxxx' # 百度云存储的api key
SK = 'xxxxxxxxxx' # 百度云存储的secret key
BNAME = 'crm-01'  # 云存储里建的Bucket


class baidu:
    @staticmethod
    def getBucket():
        ### 首先通过云存储管理界面，创建一个bucket
        ### 创建BCS管理对象
        #这里可以显式选择使用的HttpClient, 可以是:
        #HttplibHTTPC
        #PyCurlHTTPC
        bcs = pybcs.BCS(HOST, AK, SK, pybcs.HttplibHTTPC)

        #声明一个bucket
        b = bcs.bucket(BNAME)
        return b

    @staticmethod
    def upload(fileName, fileValue, fileFolder = '/custom/'):
        #获得一个bucket
        b = getBucket()

        ### 将文件内容上传到 '/custom' 下
        #声明一个object
        o = b.object(fileFolder + fileName)
        o.put(fileValue)
        
        return 'http://bcs.duapp.com/' + BNAME + o1

    @staticmethod
    def getFile(fileName):
        #获得一个bucket
        b = getBucket()
        #声明一个object
        o = b.object(fileName)

        return o.get()

    @staticmethod
    def moveTmpFileToCustom(fileName):
        ### 复制文件
        #获得一个bucket
        b = getBucket()
        #声明一个object
        oTmp = b.object('/tmp/' + fileName)
        oTmp.copy_to('/custom/' + fileName)
        time.sleep(1)
        oTmp.delete()
    
    @staticmethod
    def copyTmpFileToCustom(fileName):
        ### 复制文件
        #获得一个bucket
        b = getBucket()
        #声明一个object
        oTmp = b.object('/tmp/' + fileName)
        oTmp.copy_to('/custom/' + fileName)
    
    @staticmethod
    def delFile(fileName):
        ### 删除文件
        #获得一个bucket
        b = getBucket()
        #声明一个object
        o = b.object(fileName)
        o.delete()

    @staticmethod
    def getFiles(filePath = '/custom'):
        ### 列出所有的object
        #获得一个bucket
        b = getBucket()
        objs = b.list_objects()
        str = ','.join([o.object_name for o in objs])

        return str

if __name__ == '__main__':
    for file in getFiles():
        print file