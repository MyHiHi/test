url="http://map.baidu.com/detail?qt=ninf&uid=517c4953f35f425654bfff78&detail=cater"
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
c = requests.get(url=url,headers=headers).content.decode('utf-8')
print(c)