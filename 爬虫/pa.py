# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2016-12-16 16:21:53
# @Last Modified by:   Marte
# @Last Modified time: 2016-12-18 18:53:45

# import urllib
# import urllib2

'''
   1. request 请求
'''
# values = {"username":"bdx1025588958","password":"XXXXX"}
# data   = urllib.urlencode(values)
# url    = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"

# request  = urllib2.Request(url,data)
# response = urllib2.urlopen(request)

# print response.read()





'''
   2. get 请求
'''
# values = {}

# values["username"] = "bdx0125588958"
# values["password"] = "xxx"

# data   = urllib.urlencode(values)
# url    = "https://passport.csdn.net/account/login"
# geturl = url + "?" + data

# request  = urllib2.Request(geturl)
# response = urllib2.urlopen(request)

# print response.read()


'''
   3. header请求
'''


#有些网站不会同意程序直接用上面的方式进行访问，如果识别有问题，那么站点根本不会响应，所以为了完全模拟浏览器的工作，我们需要设置一些Headers 的属性。
# 以下程序会自动报错
# url         = 'http://www.server.com/login'
# user_agent  = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# values      = {'username' : 'cqc',  'password' : 'XXXX' }
# headers     = { 'User-Agent' : user_agent }
# data        = urllib.urlencode(values)
# request     = urllib2.Request(url, data, headers)
# response    = urllib2.urlopen(request)
# page        = response.read()
# print page

# import urllib2
# import urllib

'''
    4. try catch 请求
'''


# 使用DebugLog 将收发包内容打在屏幕上
# httpHandler  = urllib2.HTTPHandler(debuglevel=1)
# httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
# opener = urllib2.build_opener(httpHandler, httpsHandler)
# urllib2.install_opener(opener)

# #请求的网站
# url = "https://www.account.xiaomi.com/pass/serviceLoginAuth2"


# # post 请求
# postdata = urllib.urlencode({"user":"XXXXXXX",
#                              "_json":"true",
#                              "pwd":"XXXXXXX",
#                              "sid":"eshop",
#                              "_sign":"g7K1HSZPYIaO4tSlhS1xdDJBPV8=",
#                              "callback":"http://order.xiaomi.com/login/callback?followup=http%3A%2F%2Fwww.xiaomi.com%2Findex.php&sign=ZjEwMWVlOTY3MWM1OGE3YjYxNGRiZjQ5MzJmYjI5NDE0ZWY0NzY5Mw,,"                                                                 })

# request = urllib2.Request(url, data=postdata)
# request.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/26.0")

# try:
#     response = urllib2.urlopen(request)
#     print 'try function ..... \n'
#     print response.info()
#     print response.read()
# except urllib2.HTTPError,e:
#     print 'Exception Start ..... \n'
#     print e.getcode()
#     print e.reason


'''
    5. CookieJar
'''


# import urllib2
# import cookielib

# #声明一个CookieJar对象实例来保存cookie
# cookie   = cookielib.CookieJar()

# #设置保存cookie的文件，同级目录下的cookie.txt
# filename = 'cookie.txt'

# #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler  = urllib2.HTTPCookieProcessor(cookie)

# #通过handler来构建opener
# opener   = urllib2.build_opener(handler)

# #此处的open方法同urllib2的urlopen方法，也可以传入request
# response = opener.open('http://www.baidu.com')

# print 'cookie 的内容 = ',cookie

# for item in cookie:

#     print 'Name = ' + item.name
#     print 'Value = '+ item.value

# #保存cookie到文件
# cookie.save(ignore_discard=True, ignore_expires=True)


# import cookielib
# import urllib2

# #设置保存cookie的文件，同级目录下的cookie.txt
# filename = 'cookie.txt'
# #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
# cookie = cookielib.MozillaCookieJar(filename)
# #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib2.HTTPCookieProcessor(cookie)
# #通过handler来构建opener
# opener = urllib2.build_opener(handler)
# #创建一个请求，原理同urllib2的urlopen
# response = opener.open("http://www.baidu.com")
# #保存cookie到文件
# cookie.save(ignore_discard = True, ignore_expires=  True)
# #ignore_discard的意思是即使cookies将被丢弃也将它保存下来，ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入，在这里，我们将这两个全部设置为True。


# #创建MozillaCookieJar实例对象
# cookie = cookielib.MozillaCookieJar()
# #从文件中读取cookie内容到变量
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# #创建请求的request
# req = urllib2.Request("http://www.baidu.com")
# #利用urllib2的build_opener方法创建一个opener
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open(req)
# print response.read()


'''
    6. 实战百度爬虫
'''


# __author__ = 'Kali'
# # -*- coding:utf-8 -*-
# import urllib
# import urllib2
# import re

# #处理页面标签类
# class Tool:
#     #去除img标签,7位长空格
#     removeImg = re.compile('<img.*?>| {7}|')
#     #删除超链接标签
#     removeAddr = re.compile('<a.*?>|</a>')
#     #把换行的标签换为\n
#     replaceLine = re.compile('<tr>|<div>|</div>|</p>')
#     #将表格制表<td>替换为\t
#     replaceTD= re.compile('<td>')
#     #把段落开头换为\n加空两格
#     replacePara = re.compile('<p.*?>')
#     #将换行符或双换行符替换为\n
#     replaceBR = re.compile('<br><br>|<br>')
#     #将其余标签剔除
#     removeExtraTag = re.compile('<.*?>')
#     def replace(self,x):
#         x = re.sub(self.removeImg,"",x)
#         x = re.sub(self.removeAddr,"",x)
#         x = re.sub(self.replaceLine,"\n",x)
#         x = re.sub(self.replaceTD,"\t",x)
#         x = re.sub(self.replacePara,"\n    ",x)
#         x = re.sub(self.replaceBR,"\n",x)
#         x = re.sub(self.removeExtraTag,"",x)
#         #strip()将前后多余内容删除
#         return x.strip()


# #百度贴吧爬虫类
# class BDTB:

#     #初始化，传入基地址，是否只看楼主的参数
#     def __init__(self,baseUrl,seeLZ):
#         self.baseURL = baseUrl
#         self.seeLZ   = '?see_lz='+str(seeLZ)
#         self.tool    = Tool()

#     #传入页码，获取该页帖子的代码
#     def getPage(self,pageNum):
#         try:
#             url      = self.baseURL+ self.seeLZ + '&pn=' + str(pageNum)
#             request  = urllib2.Request(url)
#             response = urllib2.urlopen(request)
#             return response.read().decode('utf-8')
#         except urllib2.URLError, e:
#             if hasattr(e,"reason"):
#                 print u"连接百度贴吧失败,错误原因",e.reason
#                 return None

#     #获取帖子标题
#     def getTitle(self):
#         page    = self.getPage(1)
#         pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>',re.S)
#         result  = re.search(pattern,page)
#         if result:
#             #print result.group(1)  #测试输出
#             return result.group(1).strip()
#         else:
#             return None

#     #获取帖子一共有多少页
#     def getPageNum(self):
#         page    = self.getPage(1)
#         pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
#         result  = re.search(pattern,page)
#         if result:
#             #print result.group(1)  #测试输出
#             return result.group(1).strip()
#         else:
#             return None

#     #获取每一层楼的内容,传入页面内容
#     def getContent(self,page):
#         pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
#         items   = re.findall(pattern,page)
#         #for item in items:
#         #  print item
#         print self.tool.replace(items[1])


# baseURL = 'http://tieba.baidu.com/p/3138733512'
# bdtb = BDTB(baseURL,1)
# bdtb.getContent(bdtb.getPage(1))
#















