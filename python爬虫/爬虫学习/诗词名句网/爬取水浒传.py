#!/user/bin/env python
# coding=utf-8
'''
@author  :  Lijing
#@ide    :  python 3.9
#@time   : $[YEAR]-$[MONTH]-$[DAY] $[HOUR]:$[MINUTE]:$[SECOND]
'''
import  requests

from bs4 import BeautifulSoup

#诗词名句网
url = 'https://www.shicimingju.com/book/shuihuzhuan.html'
#U-A伪装
headers ={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}
#请求响应
response = requests.get(url=url,headers=headers)
response.encoding='utf-8'
#数据解析
soup = BeautifulSoup(response.text,'lxml')
#找到所有章节
li_list = soup.select(".book-mulu > ul > li")#select返回的是列表
fp = open("book/水浒传.txt","w",encoding='utf-8')
for li in li_list:
    #章节名
    title = li.a.text
    #章节网址
    chapter_url = 'https://www.shicimingju.com'+str(li.a['href'])
    #headers共用
    #请求响应
    chapter_response = requests.get(url=chapter_url,headers=headers)
    chapter_response.encoding='utf-8'
    #数据解析
    charpter_soup = BeautifulSoup(chapter_response.text,'lxml')
    content = charpter_soup.find('div',class_='chapter_content').text
    #print(title+' 爬取完毕！')
    print(title+"\n"+content)
    fp.write(title+content)