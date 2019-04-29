url="http://map.baidu.com/detail?qt=ninf&uid=517c4953f35f425654bfff78&detail=cater"
import requests
from selenium import webdriver
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
url="https://www.cnblogs.com/graceting/p/4018458.html/"

url="http://hotel.qunar.com/city/baoding/dt-5117/?tag=baoding#fromDate=2019-03-04&toDate=2019-03-05&q=%E4%BF%9D%E5%AE%9A%E9%9D%92%E5%B9%B4%E5%85%AC%E5%AF%93&from=hotellist&fromFocusList=0&filterid=9ba67236-345a-41a7-9ba8-578ad3e53a20_A&showMap=0&qptype=hotelName&QHFP=ZSS_A4D9D23A"

from pyquery import PyQuery as pq
c = webdriver.Firefox()

# c = requests.get(url=url,headers=headers).content.decode('utf-8')
# print(c)
# print(c)
# c1 = pq(c)("#cnblogs_post_body td")
# s=[]
# for i in c1.items():
#     a = i.text()
#     if (len(a)>90):
#         s.append(a)

# s1=[]
# print(s)
# for i in s:
#     s1.append(i)
#     # print(i)
# print(s1)
# print(c)
# # print(c1)
# //dimg12.c-ctrip.com/images/20040500000011885AEAA_R_300_225.jpg);

# http://hotels.ctrip.com/hotel/dimg12.c-ctrip.com/images/20040500000011885AEAA_R_300_225.jpg