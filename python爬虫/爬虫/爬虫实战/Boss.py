import re
import requests

from bs4 import BeautifulSoup

url = "https://www.zhipin.com/c100010000/?query=Java&page="


def askURL(url):

    header = {
        "user-agent":"Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 92.0.4515.159Safari / 537.36"
    }
    request = requests.get(url,headers=header)
    print(request.status_code)
    #html = ""
    try:
        html=request.text
        print(html)
        with open('./a.html','w',encoding='utf-8') as fp:
            fp.write(html)
    except Exception as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    finally:
        pass
        #return html

#分析提取数据
def getData(url):
    #存储待提取的数据
    datalist = []
    #获取网页源码
    for i in range(0,1):
        URL = url + str(i+1)
        html = askURL(URL)
        #逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="job-primary"):
            data = []
            item = str(item)
            #正则匹配
            #职位名
            print(item.span.text)

if __name__ == "__main__":
    askURL(url)