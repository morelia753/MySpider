import requests


url = 'https://www.baidu.com/s'

#代理
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}
#处理url携带的参数，封装到字典

keyword = input("输入一个待搜索的关键字：")

param ={
    'wd' : keyword
}

response = requests.get(url,params=param,headers=headers)
#response.encoding='utf-8'
filename = keyword+'.html'
with open(filename,'w',encoding='utf-8') as fp:
    fp.write(response.text)

print("filename"+'保存成功！！！')