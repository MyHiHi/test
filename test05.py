import requests,ssl
from selenium import webdriver
# browser = webdriver.Firefox()
# headers = { 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#   'accept-encoding': 'gzip, deflate, br', 'accept-language': 'zh-CN,zh;q=0.9', 
#   'cookie': '__c=1535347437; __g=-; __l=l=%2Fwww.zhipin.com%2Fc101010100%2Fh_101010100%2F%3Fquery%3D%25E7%2588%25AC%25E8%2599%25AB%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588%26page%3D4%26ka%3Dpage-4&r=; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1533949950,1534555474,1535095432,1535347437; lastCity=101010100; toUrl=https%3A%2F%2Fwww.zhipin.com%2Fjob_detail%2F%3Fquery%3Dpython%26scity%3D101010100%26industry%3D%26position%3D; JSESSIONID=""; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1535348378; __a=5534803.1512627994.1535095432.1535347437.264.8.4.260', 'referer': 'https://www.zhipin.com/job_detail/?query=python&scity=101010100&industry=&position=', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' }

# # browser.get(url)
# # print(browser.page_source)
# print(requests.get(url,headers=headers).content.decode("utf-8"))

# headers={'Accept': 'text/html,application/xhtml+xm…ml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2', 'Connection': 'keep-alive', 'Cookie': 'lastCity=101010100; toUrl=http…48303.6.2.5.6; __c=1550548303', 'DNT': '1', 'Host': 'static.zhipin.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/65.0'}
# headers={}
ssl._create_default_https_context = ssl._create_unverified_context
url="http://hotel.elong.com/10101940/"
c = requests.get(url=url).content.decode('utf-8')
print(c)