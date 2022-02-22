import requests

url ='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

null = " "
#存储餐厅基本信息
database = []

def FileWrite():
    f = open("肯德基餐厅.txt","a")
    if database[3] == '江苏省' and database[4] == '南京市':
        for data2 in database:
            f.write(data2+"  ")
        f.write('\n')

city = input("input your city:")
numbers_pages = 1
number = 0
data = {
        'cname': '',
        'pid': '',
        'keyword': city,
        'pageIndex': numbers_pages,
        'pageSize': 10,
}

response = requests.post(url,data,headers=headers)
text = response.text

#print(text)
#with open("./city.txt","w",encoding='utf-8') as fp:
#        fp.write(text)
#将列表text转变为字典
dictionary = eval(text)
#解析数据
data1 = dictionary['Table1']
for i in range(len(data1)):
    StoreName = data1[i]['storeName']
    database.append(StoreName)
    Address = data1[i]['addressDetail']
    database.append(Address)
    Pro = data1[i]['pro']
    database.append(Pro)
    ProvinceName = data1[i]['provinceName']
    database.append(ProvinceName)
    CityName = data1[i]['cityName']
    database.append(CityName)
    #DataBase.append(database)
    print(database)
    FileWrite()
    database = []

#print(DataBase)
numbers = dictionary['Table'][0]['rowcount']
print(numbers)
if numbers == 0:
   print("抱歉,{city}没有肯德基餐厅。")
else:
   print(city+"有"+str(numbers)+"家肯德基餐厅。")
   number = numbers // 10
for i in range(number):
   numbers_pages += 1
   data = {
       'cname': '',
       'pid': '',
       'keyword': city,
       'pageIndex': numbers_pages,
       'pageSize': 10,
   }
   response = requests.post(url,data,headers=headers)
   text = response.text
   # 将列表text转变为字典
   dictionary = eval(text)
   # 解析数据
   data1 = dictionary['Table1']
   for i in range(len(data1)):
       StoreName = data1[i]['storeName']
       database.append(StoreName)
       Address = data1[i]['addressDetail']
       database.append(Address)
       Pro = data1[i]['pro']
       database.append(Pro)
       ProvinceName = data1[i]['provinceName']
       database.append(ProvinceName)
       CityName = data1[i]['cityName']
       database.append(CityName)
       print(database)
       FileWrite()
       database = []


