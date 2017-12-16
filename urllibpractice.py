# -*- coding:utf-8 -*-

import urllib2

def load_baidu():

    url = 'http://www.baidu.com'

    #response = urllib2.urlopen(url)
    #可以构建请求对象之后,Request 是大写
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)

    html = response.read()

    return html
def write_file(html):
    with open('baidu02.html','w') as f :
        f.write(html)

if __name__ == '__main__':
    data = load_baidu()
    write_file(data)