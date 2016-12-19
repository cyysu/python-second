# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2016-12-15 22:18:32
# @Last Modified by:   Marte
# @Last Modified time: 2016-12-16 15:43:44

# 你同样可以在Tornado模板中使用Python条件和循环语句。控制语句以{%和%}包围，并以类似下面的形式被使用：
import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # 当有网站请求根目录的时候  那么返回客户端的是进过渲染过的 index.html
        self.render('index.html')

class PoemPageHandler(tornado.web.RequestHandler):
    # 获取 post 请求
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb  = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        # 渲染模板目录下的 poem.html 文件
        self.render('poem.html', roads = noun1, wood = noun2, made = verb,difference = noun3)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    #你可以通过向Application类的构造函数传递一个名为static_path的参数来告诉Tornado从文件系统的一个特定位置提供静态文件。
    #
    # 创建的Application 在里面传递的参数
    app = tornado.web.Application(
        #             根目录                       # /poem
        handlers = [(r'/', IndexHandler), (r'/poem', PoemPageHandler)],
        # equestHandler类的render方法来告诉Tornado读入模板文件，插入其中的模版代码，并返回结果给浏览器。
        template_path = os.path.join(os.path.dirname(__file__), "templates")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()












