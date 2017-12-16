# -*- coding:utf-8 -*-

import urllib2

def load_baidu():

    url = 'http://www.baidu.com'

    response = urllib2.urlopen(url)

    html = response.read()

    return html
def write_file(html):
    with open('baidu01.html','w') as f :
        f.write(html)

if __name__ == '__main__':
    data = load_baidu()
    write_file(data)