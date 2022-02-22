import bs4
import requests
from time import sleep
import xlwt
#全局变量:
url = "https://book.douban.com/top250?start="


def open_url(url):
    header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    try :
        res = requests.get(url,headers = header)
    except Exception as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return res

def getData(url):

    datalist = []
    for i in range(0,10):
        URL = url + str(i*25)
        data = []
        res = open_url(URL)
        soup = bs4.BeautifulSoup(res.text,"html.parser")
        #print(soup)
        #书名
        book = []
        targets = soup.find_all("div",class_="pl2")
        for target in targets:

            BookName = target.a.text.split('\n')[1].strip()+target.a.text.split("\n")[2].strip()
            book.append(BookName)

        #基本情况
        scene = []
        targets = soup.find_all("p",class_="pl")
        for target in targets:
            Scene = target.text
            #print(Scene)
            scene.append(Scene)

        #评分
        score = []
        #评价人数
        pernum = []
        targets = soup.find_all("div",class_="star clearfix")
        for target in targets:
            Rating = target.find(name='span', class_='rating_nums').text
            score.append(str(Rating))
            PerNum = target.find(name='span', class_='pl').text.split('\n')[1].strip()
            pernum.append(PerNum)

        #简评
        comt = []
        targets = soup.find_all("span",class_='inq')
        for target in targets:
            #print(target.text)
            comt.append(target.text)
        #print(comt)
        for i in range(len(comt)):
            data.append(book[i])
            data.append(scene[i])
            data.append(score[i])
            data.append(comt[i])
        #sleep(5)
        datalist.append(data)
    print(datalist)
    return datalist

def savaData():

    path = "豆瓣书籍TOP250.xls"
    Book = xlwt.Workbook(encoding="utf-8")
    sheet = Book.add_sheet('豆瓣书籍TOP250')
    col = ('简评', '书名', '基本情况', '评分')
    for i in range(0,4):
        sheet.write(0,i,col[i])
    data = getData(url)
    print(len(data))
    k = 1
    for i in range(len(data)):
        for j in range(len(data[i])):
            print(len(data[i]))
            J = (j+1)%4
            print("j=%d J=%d"%(j,J))
            sheet.write(k , J , data[i][j])
            if (j+1)%4==0:
                print("正在写入第%d条..."%k)
                k += 1

    Book.save(path)








if __name__ == "__main__":

    getData(url)
    savaData()