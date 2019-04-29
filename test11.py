import requests
import json
import re
import csv
# import demjson
import pymysql

#连接写入提交
conn = pymysql.Connect(host='localhost', port=3306, user='root', passwd='root', db='jobs')
curor = conn.cursor()
lists=[]
dicts={}
ss=0
for i in range(1,20):
    url="http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx"
    headers={

        "Connection": "keep-alive",
        "origin":"http://hotels.ctrip.com",
        "Host": "hotels.ctrip.com",
        "referer": "http://hotels.ctrip.com/hotel/beijing1",
        "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",

    }
    data={
    "StartTime":"2018-10-09",
    "DepTime": "2018-10-10",
    "RoomGuestCount": "1,1,0",
    "cityId":1,
    "cityPY":" beijing",
    "cityCode":"010",
    "cityLat": 39.9105329229,
    "cityLng":116.413784021,
    "page":i,
    "txtKeyword":"侣松园宾馆"
    }

    html=requests.post(url,headers=headers,data=data)
    #ValueError: Invalid \escape: line 1 column 35442 (char 35441)问题在于编码中是\xa0之类的，当遇到有些 不用转义的\http之类的，则会出现以上错误。解决方案如下：
    regex = re.compile(r'\\(?![/u"])')
    fixed = regex.sub(r"\\\\", html.text)

    aa=json.loads(fixed)
    print(aa)
    for n in range(0,25):
        dianming = aa["hotelPositionJSON"][n]["name"]

        #python eval函数，将列表样式的字符串转化为列表
        jiage=eval(aa["HotelMaiDianData"]["value"]["htllist"])[n]["amount"]
        xinji=aa["hotelPositionJSON"][n]["star"][-2:]
        dangci=aa["hotelPositionJSON"][n]["stardesc"]
        pingfen=aa["hotelPositionJSON"][n]["score"]
        lianjie="http://hotels.ctrip.com"+aa["hotelPositionJSON"][n]["url"]
        ss += 1
        lists.append([ss, dianming,xinji,dangci,pingfen,jiage + "元",lianjie])

        # lists.append([s,"酒店名:"+name,"星级:"+xinji,"档次:"+dangci,"评分:"+pingfen,"价格:"+jiage+"元"])
        dicts[ss]=["酒店名:"+dianming,"星级:"+xinji,"档次:"+dangci,"评分:"+pingfen,"价格:"+jiage+"元","链接:"+lianjie]
        print("正在检索中"+str(ss))
        # print(dicts[ss])
        # hot = "insert into jdlist(jd_num,jd_name,jd_star,jd_good,jd_fen,jd_jiage,jd_link) values('%s','%s','%s','%s','%s','%s','%s')" % (ss,dianming,xinji,dangci,pingfen,jiage,lianjie)
        # curor.execute(hot)
        # conn.commit()
        # self.conn.close()
        # mm=re.findall('.*?"amount":"(.*?)"}',jiage)
# print(lists)
with open("bjjiudian.csv", "w", encoding="utf-8",newline="") as f:
    k = csv.writer(f, dialect="excel")
    k.writerow(["数量", "酒店名", "星级", "档次", "评分", "价格","链接"])

    for list in lists:
        k.writerow(list)
