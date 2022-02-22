import requests
#确定url
base_url = 'https://movie.douban.com/top250'
#找到代理
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
}
#发送请求，获得响应
response = requests.get(base_url,headers=header)

#查看页面内容，可能出现乱码
print(response.text)
with open('index1.html','w',encoding='utf-8') as fp:
    fp.write(response.text)
#print(response.encoding)
#解决乱码
#方法一:转化成utf-8格式
#response.encoding = 'utf-8'
#print(response.text)
#方法二:解码为utf-8
#with open('index.html','w',encoding='utf-8') as fp:
    #fp.write(response.content.decode('utf-8'))
print(response.status_code)
print(response.headers)
#print(type(response.text))
#print(type(response.content))
