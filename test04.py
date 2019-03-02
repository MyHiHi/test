import requests
from pyquery import PyQuery 
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
url = "https://www.ibilibili.com/video/av8842004/?p=4"
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
headers = {'Host': 'www.bilibili.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Connection': 'keep-alive',
           }

# my_proxy = webdriver.get_proxy().strip()
# proxy = Proxy({
#     'proxyType': ProxyType.MANUAL,
#     'httpProxy': my_proxy,
#     'noProxy': ''
# })
FirefoxOptions = webdriver.FirefoxOptions()
import time
FirefoxOptions.add_argument("'--proxy-server={}".format("http://202.20.16.82:10152"))
browser = webdriver.Firefox(firefox_options=FirefoxOptions)
browser.get(url)
time.sleep(3)


# text = requests.get(url,headers=headers).content;
# print(text)
text = browser.page_source
doc = PyQuery(text)
print(doc)
video_links = doc("video").attr("src")
print(video_links)