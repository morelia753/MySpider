

results = ['北京','天津','上海','广州','深圳','长春']

with open("file1.txt","w",encoding='utf-8') as f:
    for result in results:
        f.write("%s "%result)