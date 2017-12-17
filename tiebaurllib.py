# -*- coding:utf-8 -*-

import  urllib2

import urllib

import time

class Tieba(object):
    def __init__(self,tieba_name,start_page,end_page):
        self.tieba_name = tieba_name
        self.start_page = start_page
        self.end_page = end_page
        self.base_url = 'https://tieba.baidu.com/f?'
        self.header = {'User-Agent': "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3"}

    def send_request(self,url):
        time.sleep(2)
        try:
            request = urllib2.Request(url,headers=self.header)
            response = urllib2.urlopen(request)

            status_code = response.getcode()
            if status_code == 200:
                return response.read()
        except Exception as e :
            print e

    def write_file(self,page,data):

        filename = 'tieba/'+str(page)+ u'页.html'

        # 转换为Unicode后 不能用%s 转义  s是指string
        # print '%s正在下载.....'%filename
        with open(filename,'w') as f :
            f.write(data)

    def start_work(self):

        for page in range(self.start_page,self.end_page+1):
            pn = (page -1)*50
            params ={
                'kw': self.tieba_name,
                'pn' : pn
            }

            params_str = urllib.urlencode(params)
            url  = self.base_url + params_str

            data = self.send_request(url)

            #注意传参时要与 参数相对应!!!!!!!
            self.write_file(page,data)



if __name__ == '__main__':
    tieba_name = raw_input('请输入贴吧名称:')
    start_page = int(raw_input('输入起始页:'))
    end_page = int(raw_input('请输入结束页:'))

    tool = Tieba(tieba_name,start_page,end_page)
    tool.start_work()



