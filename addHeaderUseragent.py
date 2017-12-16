# -*- coding:utf-8 -*-

import urllib2
def load_baidu():

    url = 'http://www.baidu.com'
    request =urllib2.Request(url)

    #修改 请求头 隐藏 user-agent
    request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko")
    request.add_header("Connection", "keep-alive")

    #先请求 response 在 查看请求头
    response = urllib2.urlopen(request)

    user_agent = request.get_header('User-agent')
    print user_agent

if __name__ == '__main__':
    load_baidu()
