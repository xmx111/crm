#-*-coding:utf-8-*-
import time
import os
from bae.core import const
from bae.api import bcs
from bae.api import logging

HOST = const.BCS_ADDR
AK = 'xxxxxxxxxxxxx' #百度云存储的api key
SK = 'xxxxxxxxxxxxx' #百度云存储的secret key
BNAME = 'crm-01'

class baidu:
    @staticmethod
    def upload(fileName, fileValue, fileFolder = '/custom/'):
        ### 首先通过云存储管理界面，创建一个bucket
        #bname = 'crm-01'

        ### 创建BCS管理对象
        baebcs = bcs.BaeBCS(HOST, AK, SK)

        ### 将文件内容上传到 '/custom' 下
        o1 = str(fileFolder + fileName)
        e, d = baebcs.put_object(BNAME, o1, fileValue)
        #baebcs.make_public(BNAME, o1)
        
    	return 'http://bcs.duapp.com/' + BNAME + o1
    @staticmethod
    def getFile(fileName):
        ### 从获取数据
        baebcs = bcs.BaeBCS(HOST, AK, SK)
        e, d = baebcs.get_object(BNAME, fileName)
        return d
    
    @staticmethod
    def moveTmpFileToCustom(fileName):
        ### 复制文件
        baebcs = bcs.BaeBCS(HOST, AK, SK)
        e, d = baebcs.copy_object(BNAME, '/tmp/' + fileName, BNAME, '/custom/' + fileName)
        time.sleep(1)
        e, d = baebcs.del_object(BNAME, '/tmp/' + fileName)
        return d
    
    @staticmethod
    def copyTmpFileToCustom(fileName):
        ### 复制文件
        baebcs = bcs.BaeBCS(HOST, AK, SK)
        e, d = baebcs.copy_object(BNAME, '/tmp/' + fileName, BNAME, '/custom/' + fileName)
        return d
    
    @staticmethod
    def delFile(fileName):
        ### 删除文件
        baebcs = bcs.BaeBCS(HOST, AK, SK)
        e, d = baebcs.del_object(BNAME, fileName)
        return d
    @staticmethod
    def getFiles(filePath = '/custom'):
        ### 列出所有的object
        baebcs = bcs.BaeBCS(HOST, AK, SK)
        e, d = baebcs.list_objects(BNAME)
        str = ','.join(d)
        return str

if __name__ == '__main__':
    for file in getFiles():
        print file