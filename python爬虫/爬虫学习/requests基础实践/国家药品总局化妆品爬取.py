#coding=utf-8
import json

import requests

url = 'http://scxk.nmpa.gov.cn:81/xk//itownet/portalAction.do?method=getXkzsList'

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

data = {
    'on': 'true',
    'page': '1',
    'pageSize': '15',
    'productName':'',
    'conditionType': '1',
    'applyname':'',
    'applysn':''
}
id_list = []
response = requests.post(url=url,data=data,headers=headers)
doc_json = response.json()
#with open("./药品总局化妆品.html","w",encoding='utf-8') as f:
    #f.write(response.text)
#fp = open("./药品总局化妆品.json","w",encoding='utf-8')
#json.dump(doc_json,fp=fp,ensure_ascii='false')
for doc in doc_json['list']:
    #print(doc['ID'])
    id_list.append(doc['ID'])

data_json = []
company_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
for id in id_list:
    data={
        'id': id
    }
    company_json = requests.get(url=company_url,data=data,headers=headers).json()
    data_json.append(company_json)
    print(company_json)
#持久化存储
f = open("./公司数据.json","w",encoding='utf-8')
#保存,生成json文件
json.dump(data_json,f,ensure_ascii = False)
print("--------end--------")