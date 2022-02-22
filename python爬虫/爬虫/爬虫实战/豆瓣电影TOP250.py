import re
import urllib.request
from bs4 import BeautifulSoup
import xlwt


#电影名
findTitle = re.compile(r'<span class="title">(.*)</span>')

#评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')

#评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')

#电影简评
findInq = re.compile(r'<span class="inq">(.*)</span>')

#电影导演与主演
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)
def main():
    url = "https://movie.douban.com/top250?start="
    #1.爬取网页
    Datalist = getData(url)
    Savepath = "豆瓣电影Top250.xls"
    #3.保存数据
    #saveData(datalist,savepath)
    #saveData(Datalist,Savepath)

def askURL(url):
    header = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 92.0.4515.159Safari / 537.36"
    }
    request = urllib.request.Request(url,headers=header)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read()
        #print(response.txt)
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    finally:
        return html

#提取数据
def getData(url):

    datalist = []
    #获取网页源码
    for i in range(0,10):
        URL = url + str(i*25)
        html = askURL(URL)
        #print(html)
        #2.逐一解析数据
        soup =BeautifulSoup(html,"html.parser")

        for item in soup.find_all('div',class_="item"):
            print(item)
            data = []
            item = str(item)
            # 正则匹配
            #电影名
            titles = re.findall(findTitle,item)
            if(len(titles) == 2 ):#可能存在中英文名
                ctitle =titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")
                #otitle = titles[1].replace("/", "")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ')
            #电影评分
            rating = re.findall(findRating,item)
            data.append(str(rating))
            #电影评价人数
            Judge = re.findall(findJudge,item)
            data.append(Judge)
            #电影简评
            inq = re.findall(findInq,item)
            if len(inq) != 0 :
                inq = inq[0].replace("。","")
                data.append(inq)
            else:
                data.append(" ")
            #电影导演和主演
            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 去掉<br/>
            bd = re.sub('/', " ", bd)  # 替换/
            data.append(bd.strip())  # 去掉前后的空格
            #print(data)
            datalist.append(data)
    print(datalist)
    return datalist

#保存数据
def saveData(datalist,savapath):

    print("sava....")
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet('豆瓣电影TOP250')
    col = ("电影中文名","电影外文名","评分","评价人数","简评","导演与主演")
    #写入列名
    for i in range(0,6):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print("第%d条" %(i+1))
        data = datalist[i]
        for j in range(0,6):
            sheet.write(i+1,j,data[j])
    book.save(savapath)


if __name__ == "__main__":
    main()
    print("爬取完毕！")