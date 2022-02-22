import json

import requests

#指定网址
post_url = 'https://fanyi.baidu.com/pcnewcollection'
#代理
headers ={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

word = input("input a word:")

data={
    'req': 'check',
    'fanyi_src': 'dog',
    'direction': 'en2zh',
    '_': 1636165240609
}
#请求发送
response = requests.post(url=post_url,data=data,headers=headers)
#获取响应数据：json()
dic_obj = response.json()


#持久化存储
fp=open('./dog.json','w',encoding='utf-8')

json.dump(dic_obj,fp,ensure_ascii='false')