#-*-coding:utf-8-*-
import web
import sys
web.config.debug = False
urls = (
    '/', 'index',
    '/post/?',"login"
    )
render = web.template.render('template/')
class index:
    def GET(self):
        #传值
        return render.index('老婆', '哈哈')
class login:
    def POST(self):
        data = web.input()
        print data
        if data['userName'] == u'李彩娟' and data['password'] == '111111':
            retStr = '登录成功'
        else:
            retStr = '用户名或密码错误'
        return '<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head><body>' + retStr + '</body></html>'

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()