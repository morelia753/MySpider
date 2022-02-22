import urllib.request
import bs4
url = 'https://www.zhipin.com/c100010000-p100101/?srcReferer=https://www.zhipin.com/'

header = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36'
}

requests = urllib.request.Request(url,headers=header)

response = urllib.request.urlopen(requests)

soup = bs4.BeautifulSoup(response.read(),"html.parser")

for each in soup.find_all("div",class_="title"):
    print(each)