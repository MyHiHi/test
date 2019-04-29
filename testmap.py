import requests

url='http://api.map.baidu.com/place/v2/detail?uid=435d7aea036e54355abbbcc8&output=json&scope=2&ak=您的密钥'
params={
    'uid':['3a84bcefecf96577c7f50d7b','5e7c9edff294f734704b873a'],
    "output":'json',
    'scope':'2',
    'ak':'POU6Eri0Fh7rjxbr0EbbwNol7OjoZqkb',

}
p=requests.get(url=url,params=params).content.decode('utf-8') 
print(p)