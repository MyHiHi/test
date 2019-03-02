import pymysql, hashlib, string, random
from functools import reduce

xing = ["许", "张", "赵", "钱", "孙", "李", "朱", "杨"]
ming1 = ["彬", "群", "宁", "盼", "龙", "欢", "丹"]
ming2 = ["彬", "群", "宁", "盼", "龙", "欢", "丹", ""]
name = [xing, ming1, ming2]


def get_random_name():
    random_name = ""
    for i in name:
        random_name += random.choice(i)
    return random_name.strip()


def get_random_passwd(count=6):
    return "".join(random.sample(string.ascii_lowercase, count - 3)) + "".join(random.sample(list(string.digits),3))

class MyDB(object):
    def __init__(self,host,user,psswd,database):
        self.db = pymysql.connect(host,user,psswd,database)
       
        self.cursor = self.db.cursor()

    def md5(self, str):
        md = hashlib.md5()
        md.update(str.encode())
        return md.hexdigest()

    def insert(self, *data):
        print("insert into users(name,passwd)\
        values('{0}',md5('{1}')".format(
                data[0], data[1]
            ))
        self.cursor.execute(
            "insert into users(name,passwd)\
        values('{0}',md5('{1}'))".format(
                data[0], data[1]
            )
        )
        self.db.commit()
        print("ok!")

    def select(self):
        self.cursor.execute("select name,count(*) from users group by name order by count(*)")
        for i in self.cursor.fetchall():
            print(i)
        print("ok!")

    def select_name(self,name):
        n= self.cursor.execute("select * from users where name='{0}'".format(name))
        print(n)
        for i in self.cursor.fetchall():
            print(i)

    def close(self):
        self.cursor.close()
        self.db.close()


def start(count=6):
    db_01 = MyDB("localhost","root","root","jobs")
    
    # for i in range(count):
    #     db_01.insert(get_random_name(), get_random_passwd())
    
    db_01.select()
    # db_01.select_name(input("输入:"))

start(100)

