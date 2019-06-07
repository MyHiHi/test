from selenium import webdriver
from time import sleep

from pymysql import connect

# with connect(host="localhost", user="root", password="root",database="sakila",autocommit=True).cursor() as cur:
#     # cur=f.cursor()
#     name=input("输入");
#     name_list=name.split(",")
#     print(name_list)
#     sql="select * from actor where last_name=%s"
#     print(sql)
#     cur.executemany(sql,name_list)
#     print("ok")
#     for i in cur.fetchall():
#         print(i)


p = "info:xiaoZhang 33 shandong"
import re

# c = re.split(r':| ',p)
# print(''.join(c))
# p = ["rrrr@163.com", "pkc@edu.com", "retg@163.com", "099@qq.com"]
# for i in p:
#     c = re.match(r".*?@163.*", i)
#     if c:
#         print(i)


# c = sum(range(100))
# print(c)

# p=r"jpython ppv%asff&dsd pp"
# c1=p
# c2=p
# print(id(c1),id(c2),id(p))
# del p

# print(id(c1),id(c2))
# p="<html><h1>www.ccc.com</h1></html>"
# import re
# re = re.compile(r'<\w*><\w*>.*</h1></\w*>')
# p=re.match(p)
# print(p.group())
class Animal(object):
    def __init__(self,name):
        self.name=name
    def __del__(self):
        print("%s killed"%self.name)

# cat1=Animal("小米")
# cat2=cat1
# cat3=cat2
# del(cat1)
# print("cat1")
# del(cat2)
# print("cat1")
# del(cat3)
        
# from test12 import getAutoReceive
# start='寂寞的深夜';
# t=2;
# names=['小美','凯军']

# print(names[t%2]+': ',start);
# import time

# while t<10:
#     t+=1;
#     time.sleep(5*1)
#     start=getAutoReceive(start)
#     print(names[t%2]+': ',start);

import os,sys
print(sys.path[0])