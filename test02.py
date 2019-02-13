from functools import reduce
# def test():
#     pass

import os;
from collections import Counter,deque,defaultdict,namedtuple
# print(os.path.isfile("test.cpp"))

# with open("test.cpp","rb") as f:
#     print(Counter(f))

animal = namedtuple("animal","age name")
test = animal("huaer",11)
print(test.name)

# for i in dir():
#     print(dir(i))
# class test(object):
#     def __init__(self):
#         pass
#     def get(self):
#         print()
# print(dir(test()))

def get_member(func):
    from functools import wraps
    @wraps(func)
    def wrapper(*args,**kwargs):
        from  inspect import getmembers
        print(args[0] +":: ",getmembers(args[0])==dir(args[0]),"\n") 
        print(func.__name__+": ",getmembers(func)==dir(func),"\n")
    return wrapper

@get_member
def exam(str):
    pass
exam("销售")