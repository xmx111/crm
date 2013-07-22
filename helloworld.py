#-*- coding:utf-8 -*- 
import web
#定义 url,将地址映射到对应的类 
urls = (
    "/", "index", 
)

app = web.application(urls, globals())
#定义 index 类 
class index:
    #get 请求
    def GET(self):
        return "Hello World"
if __name__ == "__main__": 
    app.run()
