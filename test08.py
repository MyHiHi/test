# http://api.map.baidu.com/place/v2/detail?uid=98cedfa2c9f700e003ff2d14&output=json&scope=2&ak=eikVTDrvMvVnPldFlh44DWdUAKpq1xfL

import requests
url="http://api.map.baidu.com/place/v2/detail"
# url="http://api.map.baidu.com/place/v2/search?query=银行&bounds=39.915,116.404,39.975,116.414&output=json&ak={您的密钥}"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
uid="dc0f0adc9a351921f82213c9"
# params = {
#     'uid':uid,
#     'scope':'2',
#     'output':'json',
#     'ak':'DfPUKIDaRFpXtvAv1QqZBpS6D6SQwyMB',

# }



print(requests.get(url=url,params = params,headers = headers).content.decode('utf-8'))