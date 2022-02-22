import bs4
import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250/index_{}.html'
def URL(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    return response
for i in range(10):
    res = URL(url)
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    targets = soup.find_all('div',class_='hd')
    for target in targets:
        print(target.a.span.text)
