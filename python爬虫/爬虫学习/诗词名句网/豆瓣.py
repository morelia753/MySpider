import requests
from bs4 import  BeautifulSoup
#网址
url = 'https://movie.douban.com/top250'
#U-A伪装
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}
#请求访问
response = requests.get(url=url,headers=headers)
#存储网页源码
#with open("douban.html","w",encoding='utf-8') as fp:
#    fp.write(response.text)
#数据解析
soup = BeautifulSoup(response.text,"lxml")
movies = soup.find_all('div',class_='item')

for movie in movies:
    movie_soup = BeautifulSoup(movie.text,'lxml')
    print(movie_soup.select('.info > .hd')[0])