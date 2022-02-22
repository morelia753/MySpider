# 1. requests 发送请求，从服务器获取数据
# 2. BeautifulSoup 解析整个页面的源代码

import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.umei.cc/bizhitupian/meinvbizhi/")
resp.encoding = 'utf-8'
print(resp.text)
#解析html
main_page = BeautifulSoup(resp.text,"html.parser")
#从页面中找到需要东西

alst = main_page.find("div", attrs ={"class": "TypeList"}).find_all("a", attrs ={"class": "TypePicInfos"})
n = 1
for a in alst:
    #print(a.get("href"))
    href = a.get("href") # https://www.umei.cc/bizhitupian/meinvbizhi/228290.
    resp1 = requests.get(href)
    resp1.encoding = 'utf-8'
    child_page = BeautifulSoup(resp1.text, "html.parser")
    #找到图片的真实路径
    src = child_page.find("div", attrs = {"class": "ImageBody"}).find("img").get("src")
    print(src)
    #创建文件
    f= open("tu_%s.jpg" % n, mode= "wb") #wb表示写入非文本文件
    f.write(requests.get(src).content)
    print("you are ok")

    n += 1