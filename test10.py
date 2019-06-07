# InData="2019-03-05"
# OutData="2019-03-06"
# city="北京"
# n=1
# data = {

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

#     }

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

# url = 'http://hotel.elong.com/ajax/list/asyncsearch'
# import requests
# c=requests.post(url, data = data, headers = headers)
# print(c.json())


import base64
import requests
def get_accessToken():
    token_url='https://aip.baidubce.com/oauth/2.0/token'
    api_key='d8McO2IaD1NZ9d3gVK9uoqFr'
    secret_key='Ta6gBIPzr98z5ofe5VsSyqeQemdzO8Pm'
    p=requests.post(token_url,params={'grant_type':'client_credentials',
    'client_id':api_key,'client_secret':secret_key},headers={'Content-Type':'application/json; charset=UTF-8'})
    access_token=p.json()['access_token']
    return access_token

def base64Encode(img_path):
    
    with open(img_path,'rb') as fp:
        return base64.b64encode(fp.read())

def getWord(img_path,word_url):
    img=base64Encode(img_path)
    p=requests.post(word_url,data={'image':img},headers={'Content-Type':'application/x-www-form-urlencoded'})
    # for i in p.json()['words_result']:
    #     print(i['words'])
    return p.json()

def ocr_recognize(type,img_path):
    access_token=get_accessToken();
    word_url='https://aip.baidubce.com/rest/2.0/ocr/v1/'+type+'?access_token='+access_token;
    print('wor: ',word_url)
    word=getWord(img_path,word_url)
    return word;

def body_recognize(type,img_path):
    access_token=get_accessToken();
    word_url='https://aip.baidubce.com/rest/2.0/image-classify/v1/'+type+'?access_token='+access_token;
    print('wor: ',word_url)
    word=getWord(img_path,word_url)
    return word;

if __name__=='__main__':
    import sys,os
    # u_type=['train_ticket','handwriting','license_plate','general'][-1]
    # img_path=os.path.join(sys.path[0],'images\huo.png')
    # w=ocr_recognize(u_type,img_path)
    # print(w)
    # u_type=['body_analysis'][-1]
    img_path=os.path.join(sys.path[0],'images\man.jpg')
    # w=body_recognize(u_type,img_path)
    # print(w)
    # img=base64Encode(img_path);
    # print('encode: ',img)
    # s_img=base64.b64decode(img)
    # print('decode: ',s_img)
    # from base64 import test

    # with open(os.path.join(sys.path[0],'images\man1.jpg'),'wb') as f:
    #     f.write(s_img)
    from sklearn.datasets import load_iris,fetch_california_housing,load_digits
    iris=load_iris()
    iris=load_digits()
    print(iris.keys())
    print(iris.images)
    samples,features=iris.data.shape;
    print((samples,features))
     
    iris_data=iris.data
   
    import pandas as pd
    iris_data = pd.DataFrame( iris.data, 
                            columns=iris.target_names )
    iris_data['species'] = iris.target_names[iris.target]
    iris_data.head(3).append(iris_data.tail(3))
    # print(iris.target_names)
    # print(iris.data,iris_data)
    import seaborn as sns
    import matplotlib.pyplot as plt
    p=sns.pairplot(iris_data,hue='species',palette='husl')
    plt.show()
