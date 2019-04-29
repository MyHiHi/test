from django.test import TestCase

import requests
def get_json(url):
    headers = {
    "Host": "www.lagou.com",
    "Connection": "keep-alive",
    "Origin": "https://www.lagou.com",
    "X-Anit-Forge-Code": "0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "X-Anit-Forge-Token": None,
    "Referer": "https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput=",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    }
    params={
        "needAddtionalResult": "false"
    }
    data={
        "first": "true",
        "pn": "1",
        "kd": "数据分析"
    }
    res=requests.post(url,headers=headers,data=data)
    res.encoding='utf-8'
    return res.json()
url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
data=get_json(url)
print(data)