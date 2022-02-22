#coding=utf-8

import requests
from bs4 import BeautifulSoup
#网址
url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
#UA伪装
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}
#请求数据
response = requests.get(url=url,headers=headers)
response.encoding='utf-8'
#数据解析
soup = BeautifulSoup(response.text,'lxml')
#选择器,找到所有章节名
li_list = soup.select('.book-mulu > ul > li')

fp = open("book/三国演义.txt", "w", encoding="utf-8")
for li in li_list:

    #章节名
    title = li.a.string
    #章节网址
    detail_url = "https://www.shicimingju.com"+li.a['href']
    #对章节网址进行数据请求
    header={
        'user - agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 95.0.4638.69Safari / 537.36'
    }
    detail_response = requests.get(url=detail_url,headers=header)
    detail_response.encoding='utf-8'
    #数据解析
    detail_soup = BeautifulSoup(detail_response.text,'lxml')

    div_tag = detail_soup.find('div',class_='chapter_content')
    #解析到了章节内容
    content = div_tag.text
    print(title+" 爬取成功!")
    fp.write(title+content+'\n')

print("-----------over------------")
