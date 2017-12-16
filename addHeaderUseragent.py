# -*- coding:utf-8 -*-

import urllib2
def load_baidu():

    url = 'http://www.baidu.com'
    request =urllib2.Request(url)
    response = urllib2.urlopen(request)

    user_agent = request.get_header('User-agent')
    print user_agent

if __name__ == '__main__':
    load_baidu()
