1. 首先阅读 doc/pythonstart.pdf，不会python的话最好读一遍。
2. 然后按照里面的18章-2)来配置环境 (用到的第三方包web.py0.37、SQLAlchemy0.9.3、MySQL-python1.2.3、Baidu-BCS-SDK-Python1.3.2)
3. 下载代码，修改com\ufo\service\DBConfig.py里的mysql连接字符串
4. 在cmd命令行里进入crm，运行python com\ufo\service\Service.py来建库
5. 在crm下运行python server.py 80来启动服务
6. 浏览器里输入http://localhost/
7. 用户名密码在com\ufo\service\Service.py

百度应用引擎2.0可以看crm-bae2.0分支
百度应用引擎3.0可以看crm-bae3.0分支
