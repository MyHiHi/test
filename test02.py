from functools import reduce
# def test():
#     pass

import os;
from collections import Counter,deque,defaultdict,namedtuple
# print(os.path.isfile("test.cpp"))

# with open("test.cpp","rb") as f:
#     print(Counter(f))

# animal = namedtuple("animal","age name")
# test = animal("huaer",11)
# print(test.name)

# for i in dir():
#     print(dir(i))
# class test(object):
#     def __init__(self):
#         pass
#     def get(self):
#         print()
# print(dir(test()))

# def get_member(func):
#     from functools import wraps
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         from  inspect import getmembers
#         print(args[0] +":: ",getmembers(args[0])==dir(args[0]),"\n") 
#         print(func.__name__+": ",getmembers(func)==dir(func),"\n")
#     return wrapper

# @get_member
# def exam(str):
#     pass
# exam("销售")

mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
# print({k.lower():mcase.get(k.lower(),0)+mcase.get(k.upper(),0)
# for k in mcase.keys()})
# for i,v in mcase.items():
#     print(i,v)
# example = [12,23,2]
# p = example;
# p.append(100)
# print(example)
# del example
# print(p)
# print(example)
list1,list2=[1,13,2],[14,3,5]
data = zip(list1,list2)
# data.sort()
# print(data)
for i in data:
    print(i)
# list1,list2 = map(lambda t:list(t),zip(*data))
# print(next(data))
  
print(list1)
# 你是否想过通过网络快速共享文件？好消息，Python为你提供了这样的功能。
# 进入到你要共享文件的目录下并在命令行中运行下面的代码：
#  # Python 2
#     python -m SimpleHTTPServer

#     # Python 3
#     python -m http.server 8998
# ipconfig:http://192.168.111.105(本机IP):8000/