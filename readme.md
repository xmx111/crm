简单客户管理系统	{#welcome}
=====================


本系统是一个简单的客户资料管理系统，需求源于我老婆，主要用来记录她拥有客户的资料，借着这个机会就用 **python** 的 **web.py** 框架把它完成了，顺便学习 **python** 的web和db方面的东西，放在 **github** 上开源分享。

>**ps:** 
>
> - 毕竟只是一个自用的小系统，会有 **BUG** 存在
> - 有些地方没注释
> - **python** 高手可以无视此项目

----------


一、**Python** 环境搭建
---------

1. 安装 **python**，请网上自搜，版本 *2.7.x*
2. **python** 第三方包环境配置请看 **doc/pythonstart.pdf** 里的第 **18** 章第 **2** 部分
3. 用到的第三方包: **web.py0.37**、**SQLAlchemy0.9.3**、**MySQL-python1.2.3**、**Baidu-BCS-SDK-Python1.3.2**

>**NOTE:** 
>
> - 如果不打算安装多版本 **python** 的话，可以不装**18** 章第 **2** 部分提到的 **virtualenv**，
> - 主版本可以不用安装 **Baidu-BCS-SDK-Python1.3.2** 这个第三方包

----------

二、数据库
---------

1. 使用 **Mysql** 从2看起，使用 **sqlite** 从5看起
2. 安装 **Mysql**，请网上自搜，版本 *5.5*
3. 修改 **com\ufo\service\DBConfig.py** 里的 *mysql* 连接字符串  
 host = '192.168.1.221:3316' *# **ip** 和 **端口** *
 user = 'root' *# 用户名*
 password = 'csany' *# 密码*
 db = 'crm2' *# 数据库名*
4. **Windows** 在 **cmd** 命令行里进入 **crm** 目录，运行 **python com\ufo\service\Service.py** 来建库，**Linux** 则在 **shell** 里输入
5. 如果使用 **sqlite** 则注释 **com\ufo\service\Service.py** 里的 *13 * 行，取消注释 *14* 行，然后进行上面 **4** 的操作

> **NOTE**
>
> 初始用户名密码在 **com\ufo\service\Service.py** 的 *316* 行里设置

----------

三、启动运行
---------

1. 在 **crm** 目录下运行 **python server.py 80** 来启动服务
2. 浏览器里输入 **http://localhost/** 
3. 用户名密码在 **com\ufo\service\Service.py** 的 *316* 行

---------

四、版本分支说明
---------

1. **master** 主版本，本地可运行的版本
2. **crm-bae2.0** 使用百度开放云平台bae2.0
3. **crm-bae3.0** 使用百度开放云平台bae3.0
