
# # coding: utf-8

# __author__ ='姜枫渔火'

# import requests, re, time, random, pandas

# from fake_useragent import UserAgent

 

# def getOnePage(url):

#     res = requests.post(url, data = data, headers = headers)

#     html = res.json()

# #     print(html)

#     return html

 

# def prasePage(html):

#     hptel_name = re.findall('title=\"(.+?)\"><span',html['value']['hotelListHtml'])

# #     print(len(hptel_name), hptel_name)

#     hptel_prince = re.findall('class="h_pri_num ">(.*?)</span>',html['value']['hotelListHtml'])

# #     print(len(hptel_prince), hptel_prince)

#     data = list(map(lambda x:(hptel_name[x], hptel_prince[x]),range(len(hptel_name))))

#     print(data)

#     return data

 

# def writeToFile(data):

#     content = pandas.DataFrame(data)

#     print('writing')

#     content.to_csv('艺龙.csv', header=False, index=False, mode='a+')

#     print("done")

 

# if __name__ == '__main__':

#     city = input("请输入待查询城市：")

#     InData = input("请输入入住时间(xxxx-xx-xx)：")

#     OutData = input("请输入离开时间(xxxx-xx-xx)：")

#     for n in map(lambda i : str(i), range(1, 21)):

#         print("第" + n + "页")

#         url = 'http://hotel.elong.com/ajax/list/asyncsearch'

#         data = {

#             "code":"7140144",

#     "listRequest.areaID":"",

#     "listRequest.bookingChannel":"1",

#     "listRequest.cardNo":"192928",

#     "listRequest.checkInDate":InData + " 00:00:00",    # 入住时间

#     "listRequest.checkOutDate":OutData + " 00:00:00",    # 离开时间

#     "listRequest.cityID":"0101",

#     "listRequest.cityName":city,    # 北京等地区

#     "listRequest.customLevel":"11",

#     "listRequest.distance":"20",

#     "listRequest.endLat":"0",

#     "listRequest.endLng":"0",

#     "listRequest.facilityIds":"",

#     "listRequest.highPrice":"0",

#     "listRequest.hotelBrandIDs":"",

#     "listRequest.isAdvanceSave":"false",

#     "listRequest.isAfterCouponPrice":"true",

#     "listRequest.isCoupon":"false",

#     "listRequest.isDebug":"false",

#     "listRequest.isLimitTime":"false",

#     "listRequest.isLogin":"false",

#     "listRequest.isMobileOnly":"true",

#     "listRequest.isNeed5Discount":"true",

#     "listRequest.isNeedNotContractedHotel":"false",

#     "listRequest.isNeedSimilarPrice":"false",

#     "listRequest.isReturnNoRoomHotel":"true",

#     "listRequest.isStaySave":"false",

#     "listRequest.isTrace":"false",

#     "listRequest.isUnionSite":"false",

#     "listRequest.keywords":"",

#     "listRequest.keywordsType":"0",

#     "listRequest.language":"cn",

#     "listRequest.listType":"0",

#     "listRequest.lowPrice":"0",

#     "listRequest.orderFromID":"50",

#     "listRequest.pageIndex":n,    # 翻页

#     "listRequest.pageSize":"20",

#     "listRequest.payMethod":"0",

#     "listRequest.personOfRoom":"0",

#     "listRequest.poiId":"0",

#     "listRequest.promotionChannelCode":"0000",

#     "listRequest.proxyID":"ZD",

#     "listRequest.rankType":"0",

#     "listRequest.returnFilterItem":"true",

#     "listRequest.sellChannel":"1",

#     "listRequest.seoHotelStar":"0",

#     "listRequest.sortDirection":"1",

#     "listRequest.sortMethod":"1",

#     "listRequest.starLevels":"",

#     "listRequest.startLat":"0",

#     "listRequest.startLng":"0",

#     "listRequest.taRecommend":"false",

#     "listRequest.themeIds":"",

#     "listRequest.ctripToken":"1c06a555-04ce-4884-aa05-e6f92ad0e84e",

#     "listRequest.elongToken":"jc94shhj-d5a1-4092-8060-828b168dbb61"

#         }

# headers = {'Accept':'application/json, text/javascript, */*; q=0.01',

#     'Accept-Encoding':'gzip, deflate',

#     'Accept-Language':'zh-CN,zh;q=0.8',

#     'Cache-Control':'no-cache',

#     'Content-Length':'1599',

#     'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',

#     # 'Cookie':'……61b8-48a1-b398-8b9ec1903f05……',

#     'Host':'hotel.elong.com',

#     'Origin':'http://hotel.elong.com',

#     'Pragma':'no-cache',

#     'Proxy-Connection':'keep-alive',

#     'Referer':'http://hotel.elong.com/beijing/',

#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',

#     'X-Requested-With':'XMLHttpRequest'}


# def trans(c):
#     s=""
#     for i in c:
#         if i!="\\":
#             s+=i
#     return s

# c="http:\/\/map.baidu.com\/detail?qt=ur&url=http%3A\/\/u.ctrip.com\/union\/CtripRedirect.aspx%3FTypeID%3D2%26Allianceid%3D20407%26sid%3D451676%26OUID%3D%26jumpUrl%3Dhttp%253a%252f%252fhotels.ctrip.com%252fhotel%252f3802371.html%26utm_source%3Dbaidu%26utm_medium%3Dreferral%26utm_campaign%3Dbaidumaphotel"
# print(trans(c))

# import requests
# p="https://twitter.com/i/status/1010383209308143616"
# he={ 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
# }
# c=requests.post("https://twdown.net/download.php",params={"URL":p},headers=he).content
# c=requests.post("https://twdown.net/download.php",params={"URL":p},headers=he).content
# print(c)

# p=12,
# print(p[0])
# print(type(p[0]))


def lengthOfLongestSubstring(s: str) -> int:
        x=len(s)
        max=1
        if x==0:
            return 0;
        print(s[0:1])
        for i in range(x):
            for j in range(i+1,x+1):
                k=len(set(s[i:j]))
                if max < k and k==len(s[i:j]):
                    max=k
        return max
def lengthOfLongestSubstring1(s: str) -> int:
        n=len(s)
        list=[]
        ans,i,j=0,0,0
        while (i<n and j<n):
            p=s[i]
            if p not in list:
                list.append(p)
                i+=1
                ans=max(ans,i-j)
            else:
                list.remove(s[j])
                j+=1
        
        return ans
print(lengthOfLongestSubstring("abcdefghijkrrlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345678"))        
print(lengthOfLongestSubstring1("abcdefghijkrrlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345678"))

