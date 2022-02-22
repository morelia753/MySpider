import requests
import bs4
from bs4 import BeautifulSoup

url ='https://www.bilibili.com/v/popular/all?spm_id_from=333.851.b_7072696d61727950616765546162.3'

headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
res = requests.get(url,headers=headers)

soup = bs4.BeautifulSoup(res.text,'html.parser')

targets = soup.find_all('div',class_='video-card__content')
for target in targets:
    print(target.text)