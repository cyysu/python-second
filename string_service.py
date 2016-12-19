# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2016-12-15 23:09:42
# @Last Modified by:   Marte
# @Last Modified time: 2016-12-15 23:23:06
import textwrap

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input):
        self.write(input[::-1])

# WrapHandler类处理匹配路径为/wrap的请求
class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(textwrap.fill(text, int(width)))

#Tornado在元组中使用正则表达式来匹配HTTP请求的路径    （这个路径是URL中主机名后面的部分，不包括查询字符串和碎片。）Tornado把这些正则表达式看作已经包含了行开始和结束锚点（即，字符串"/"被看作为"^/$"）
if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        # r"/reverse/(\w+)" 下面的正则表达式表示匹配的是reverse 后面的字符串  [A-Z][a-z][0-9] 一次或者多次
        handlers = [
            (r"/reverse/(\w+)", ReverseHandler),   #将匹配出来的结果传递给 ReverseHandler
            (r"/wrap", WrapHandler)
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()




