# -*- coding:utf-8 -*-
# Author: 自学小白菜
'''
既然选择了前进，那每一步都要认真的去做
'''

#导包
from lxml import etree
import requests
from urllib import request
import time
import os

class MySpider(object):
    def __init__(self):
        #显然我们需要最基础的headers信息
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
        }
        #其次我们需要url
        self.url = 'http://www.bbsnet.com/doutu/page/{page}'

    def run(self):
        try:
            pages = int(input('请输入需要获取多少页：'))
            for page in range(1,pages+1):
                url = self.url.format(page = page)
                #首先我们需要一个函数获取每一个url
                target_urls = self.get_target_urls(url)
                #其次我们需要去获取每一个url里面的图片
                self.get_target_images(target_urls)
        except Exception as e:
            print('错误原因：',e)

    def get_target_urls(self,url):
        '''这里我们使用一个东西，比如列表等来存储url的结果并返回'''
        response = requests.get(url,headers=self.headers)
        text = response.content
        #下面开始解析
        html = etree.HTML(text)
        target_urls = html.xpath('//h2/a/@href')
        return target_urls

    def get_target_images(self,target_urls):
        '''这里我们需要接收之前获取的url，所以需要一个参数'''
        os.mkdir('./Images')
        for url in target_urls:
            target_images,title = self.get_info(url)
            for index,image_url in enumerate(target_images):
                self.download(image_url,index,title)
                break
            break

    def get_info(self,url):
        response = requests.get(url, headers=self.headers)
        time.sleep(2)
        response = requests.get(url, headers=self.headers)
        text = response.content
        # 开始解析
        html = etree.HTML(text)
        target_images = html.xpath('//div[@id="post_content"]//p//img/@src')
        title = html.xpath('//div[@id="post_content"]//p//img/@title')[0]
        os.mkdir('./Images/' + title)

        return target_images,title

    def download(self,image_url,index,title):
        response = requests.get(image_url, headers=self.headers)
        f = open('./Images/%s/%s.gif' % (title, index), 'wb')
        f.write(response.content)
        f.close()

if __name__ == '__main__':
    spider = MySpider()
    spider.run()
