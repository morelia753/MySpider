import requests
import bs4
import re
import time

#url = "https://movie.douban.com/top250"
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')

def open_url(url):
    #使用代理
    header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }

    res = requests.get(url,headers=header)
    return res

def find_movies(res):
    soup = bs4.BeautifulSoup(res.text,'html.parser')

    #电影名
    movies = []
    targets = soup.find_all("div",class_="hd")
    #print(targets)
    for each in targets:
        movies.append(each.a.span.text)
    #评分
    ranks = []
    targets = soup.find_all("div",class_="star")
    #print(targets)
    #print(re.findall(findRating, targets))
    for each in targets:
        rating = re.findall(findRating,str(each))
        ranks.append("评分:%s " % str(rating))

    #资料
    messages = []
    targets = soup.find_all('div',class_="bd")
    for each in targets:
        try:
            check = each.p.text.split('\n')[1].strip()+each.p.text.split('\n')[2].strip()
            messages.append(check)
            #print(check)
        except:
            continue


    result = []
    length = len(movies)
    for i in range(length):
        result.append(movies[i]+" "+ranks[i]+" "+messages[i]+'\n')

    return result

#找出一共有多少个页面
def find_depth(res):
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    depth = soup.find('span',class_='next').previous_sibling.previous_sibling.text

    return int(depth)

def main():
    host = "https://movie.douban.com/top250"
    res = open_url(host)
    depth = find_depth(res)

    result = []
    for i in range(depth):
        time.sleep(3)
        url = host + '/?start=' +str(25 * i)
        res = open_url(url)
        result.extend(find_movies(res))
    with open("豆瓣TOP250电影.txt","w",encoding="utf-8") as f:
        for each in result:
            f.write(each)

if __name__ == "__main__":
   main()
   print("爬取完毕")