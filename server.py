#-*-coding:utf-8-*-
import web
urls = (
    '/', 'index',
    '/list/(.+)', 'list_user'
    )
render = web.template.render('template/')
class index:
    def GET(self):
        #传值
        return render.index('老婆', '哈哈')

class list_user:
    def GET(self, name):
        #GET传值
        return "get name value: {0}".format(name)
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
