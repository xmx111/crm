#-*-coding:utf-8-*-

import hashlib

class Encrypt():
    @staticmethod
    def md5(str):
    	str += "illcj__$$"
        return hashlib.md5(str).hexdigest().upper()