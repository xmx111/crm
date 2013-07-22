#-*-coding:utf-8-*-
import web
urls = (
    '/', 'index'
    )
render = web.template.render('template/')
class index:
    def GET(self):
        #传值
        return render.index('老婆', '哈哈')
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
