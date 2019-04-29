from functools import reduce

# def test():
#     pass

import os
from collections import Counter, deque, defaultdict, namedtuple

# p={"s":1,"d":3}
# print(p.)
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

mcase = {"a": 10, "b": 34, "A": 7, "Z": 3}
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
list1, list2 = [1, 13, 2], [14, 3, 5]
data = zip(list1, list2)
# data.sort()
# print(data)
# for i in data:
#     print(i)
# list1,list2 = map(lambda t:list(t),zip(*data))
# print(next(data))

# print(list1)
# 你是否想过通过网络快速共享文件？好消息，Python为你提供了这样的功能。
# 进入到你要共享文件的目录下并在命令行中运行下面的代码：
#  # Python 2
#     python -m SimpleHTTPServer

#     # Python 3
#     python -m http.server 8998
# ipconfig:浏览器访问:http://192.168.111.105(本机IP):8000/

# from ctypes import CDLL
# import addList
# print(addList.add([1,2,3,4]))


# class File(object):
#     def __init__(self, file_name, method):
#         self.file_obj = open(file_name, method)

#     def __enter__(self):
#         print("entered..")
#         return self.file_obj

#     def __exit__(self, type, value, track):
#         print("Exception {0}:{1} occurs but handled".format(type,value))
#         self.file_obj.close()
#         return True


# with File("test03.cpp", "r") as f:
#     print(f.read())

# from contextlib import contextmanager
# @contextmanager
# def open_file(name):
#     f=open(name,"a")
#     yield f;
#     f.close()
# with open_file("test04.js") as f:
#     f.write("hello world\n")

# a=[]
# for i in range(100):
#     import random
#     a.append(random.randint(1,20))
# print(a,"\n",set(a))

# def get_runtime(func):
#     def wrapper(*args,**kwargs):
#         import time
#         start=time.process_time()
#         func(*args,**kwargs);
#         print(float(time.process_time()-start))
#     return wrapper

# @get_runtime
# def func(name):
#     print(name+" is runed")

# func("pyyy")
def threeSum( nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return None;
        p=[]
        leg=len(nums)
        for i in range(leg):
            for j in range(i+1,leg):
                num1,num2,num3=nums[i],nums[j],0-nums[i]-nums[j]
                if num3 in nums[j+1:]:
                    t=True
                    if p:
                        for c in p:
                            if num1 in c and num2 in c and num3 in c:
                                t=False
                                break;
                    if t:
                        p.append([num1,num2,num3])
        return p;


# po=threeSum([-1, 0, 1, 2, -1, -4])

# print(po)
# from collections import reduce
# p=reduce(lambda x,y:x+y , range(1,10**8+1))
# print(p)
print("1"-"0")