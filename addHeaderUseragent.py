# -*- coding:utf-8 -*-

import urllib2
def load_baidu():

    url = 'http://www.baidu.com'

    # 修改 请求头 隐藏 user-agent
    # request =urllib2.Request(url)
    # request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko")
    # request.add_header("Connection", "keep-alive")

    #第二种方式
    header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3"}
    request = urllib2.Request(url,headers=header)
    #先请求 response 在 查看请求头
    response = urllib2.urlopen(request)

    user_agent = request.get_header('User-agent')
    print user_agent

if __name__ == '__main__':
    load_baidu()
