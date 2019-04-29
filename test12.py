import requests

   
headers={
    "Accept": "text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8",
   "Accept-Encoding": "gzip, deflate",
   "Accept-Language": "zh-CN",
   "Cache-Control": "max-age=0",
   "Connection": "Keep-Alive",
   "Cookie": "HotelDomesticVisitedHotels1=7492873=0,0,4.7,2857,/20010z000000nz6j4CF07.jpg,&3802371=0,0,4.7,47,/20040500000011885AEAA.jpg,;\
    ASP.NET_SessionId=253cmasbeveivwx5gkcdsflf; OID_ForOnlineHotel=155124249819211aoo01551659333076102002;\
     Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; \
     __utmz=1.1551242499.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none);\
    appFloatCnt=9; _jzqco=%7C%7C%7C%7C%7C1.\
    1558071443.1551602547730.1551660965578.1551661198446.1551660965578.1551661198446.0.0.0.11.11; \
    traceExt=campaign=CHNbaidu81&adid=index; _bfs=1.9; gad_city=362fbf70ec5528d00e5439404390da49; \
    HotelCityID=1split%E5%8C%97%E4%BA%ACsplitBeijingsplit2019-3-3split2019-03-04split0;\
     MKT_Pagesource=PC; __utma=1.1232410665.1551242499.1551247883.1551660702.3; \
     Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1551661198387%7D%5D; \
     _RDG=2850e193df7a302f4d314302ffc248b8be; __utmb=1.1.10.1551660702; _gid=GA1.2.1266943928.1551602548; \
     Union=SID=155952&AllianceID=4897&OUID=baidu81|index|||; _ga=GA1.2.1232410665.1551242499; __utmt=1;\
      _bfa=1.1551242498192.11aoo0.1.1551605427949.1551659331133.6.20; _RGUID=3fa1260a-8ef5-4568-a13f-e248dbaf7699; \
      __zpspc=9.3.1551659335.1551661198.7%231%7Cbaidu%7Ccpc%7Cbaidu81%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23;\
       _abtest_userid=f43a7748-e757-4b67-8c8e-1cd96935ea2b; _RSG=eLKzEgW9X.3PQthRZau_4A; _RF1=117.136.2.150;\
        _bfi=p1%3D102002%26p2%3D0%26v1%3D18%26v2%3D17; __utmc=1; _gat=1",
   "DNT": "1",
   "Host": "hotels.ctrip.com",
   "Upgrade-Insecure-Requests": "1",
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"

    }
url="http://hotels.ctrip.com/hotel/beijing1"
# data={
#     "StartTime":"2018-10-09",
#     "DepTime": "2018-10-10",
#     "RoomGuestCount": "1,1,0",
#     "cityId":1,
#     "cityPY":" beijing",
#     "cityCode":"010",
#     "cityLat": 39.9105329229,
#     "cityLng":116.413784021,
#     "page":1,
#     }
c = requests.post(url=url,headers=headers).content.decode("utf-8")
print(c)