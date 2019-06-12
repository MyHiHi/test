import pandas as pd
import time
import os
from mpl_toolkits.mplot3d import Axes3D
import scipy.optimize as spo
import numpy as np
import matplotlib.pyplot as plt


def pr(*args):
    os.system('cls')
    for i in args:
        print(i, '\n', '----------------')


def f(x, y): return np.sin(x)+0.05*x**2+np.sin(y)+0.05*y**2


# x = np.linspace(-10, 10, 50)
# y = np.linspace(-10, 10, 50)
# X, Y = np.meshgrid(x, y)
# Z = f(X, Y)
# fig = plt.figure(figsize=(8, 4))
# ax = Axes3D(fig)
# surf = ax.plot_surface(X, Y, Z, cmap=plt.cm.coolwarm, antialiased=True)
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('f(x,y)')
# fig.colorbar(surf, shrink=0.5, aspect=5)
# plt.show()

def fo(xy):
    global output
    x, y = xy
    z = f(x, y)
    # if output==True:
    #     print('%8.4f %8.4f %8.4f '%(x,y,z));
    return z

# output=True;
# ranges=((-10,10,0.1),(-10,10,0.1))
# p=spo.brute(fo,ranges,finish=None)
# pr(p,fo(p))


# dict={'行业': ['电商', '电商', '科技', '金融', '金融', '零售']}
# pd_dict=pd.Series(dict)
# pr(pd_dict)
# arr=np.array([12,2,3,4])
# pd_arr=pd.Series(arr)

# pr(pd_dict,type(pd_dict),pd_arr,type(pd_arr))

# dates=pd.date_range('20190102',periods=4)
# pd_data=pd.Series(np.random.randint(1.0,30.0,size=(4)),index=dates)
# pd_data.name='随机数'
# pr(pd_data,type(dates),pd_data.index)


# data_dict = { 'BABA': 187.07, 'PDD': 21.83, 'JD': 30.79, 'BIDU': 184.77 }
# s3 = pd.Series(data_dict, name='中概股')
# s3.index.name = '股票代号'

# pr(s3)


# import hashlib
# m=hashlib.md5()
# with open(r'D:\Documents\雅思视频\雅思6.5分旗舰全能VIP班【完整版】\1.IELTS_ydA_1_1(Av39942191,P1).flv.mp4','rb') as f:
#         m.update(f.read())
#         pr(m.hexdigest())

symbol = ['BABA', 'JD', 'AAPL', 'MS', 'GS', 'WMT']
data = {'行业': ['电商', '电商', '科技', '金融', '金融', '零售'],
        '价格': [176.92, 25.95, 172.97, 41.79, 196.00, 99.55],
        '交易量': [16175610, 27113291, 18913154, 10132145, 2626634, 8086946],
        '雇员': [np.nan, 175336, 100000, 60348, 36600, 2200000]}

df2 = pd.DataFrame(data=data, index=symbol)
df2.index.name = '代码'


df2.index = pd.MultiIndex.from_tuples(
    [('中国公司', 'BABA'), ('中国公司', 'JD'),
     ('美国公司', 'AAPL'), ('美国公司', 'MS'),
     ('德国公司', 'GS'), ('美国公司', 'WMT')])
# pr(df2,df2.describe(),)
p = time.strftime("%Y-%m-%d", time.localtime())
# pr(type(p), p)
data = [[12.65, 28.330000000000002, 910.89], [125108751.0, 44963005.0, 8010644.0], [12.65, 28.330000000000002, 910.88], [
    12.66, 28.34, 910.89], [12.582, 28.289, 899.939], [0.31, 0.52, 39.81], [0.0251, 0.0187, 0.045700000000000005]]
df = pd.DataFrame(np.array(data).T, columns=["RT_LAST", "RT_VOL", "RT_BID1", "RT_ASK1", "RT_VWAP", "RT_CHG", "RT_PCT_CHG"],
                  index=["000001.SZ", "000002.SZ", "600519.SH"])


def haveLine(df,*args):
    from texttable import Texttable
    tb = Texttable()
    tb.header(df.columns.get_values())
    tb.add_rows(df.values, header=False)
    pr(tb.draw(),*args)



# pr(tb.draw(),df.index.values,df.values)
data = np.random.randint(1, 20, size=(3, 2))
date = pd.date_range('20190211', 3)
df = pd.DataFrame(data=data, columns=['化学', '物理'])
df.name='测试数据'
# haveLine(df)
# df.to_excel(r'D:\df_data.xlsx', sheet_name='我的测试数据',index=False)

# # time.sleep(4)

# df1 = pd.read_excel(r'D:\df_data.xlsx')

# haveLine(df1)
# print(df1.iat[0])




# ****************************


symbol = ['BABA', 'JD', 'AAPL', 'MS', 'GS', 'WMT']
data = {'行业': ['电商', '电商', '科技', '金融', '金融', '零售'],
        '价格': [176.92, 25.95, 172.97, 41.79, 196.00, 99.55],
        '交易量': [16175610, 27113291, 18913154, 10132145, 2626634, 8086946],
        '雇员': [101550, 175336, 100000, 60348, 36600, 2200000]}
df = pd.DataFrame( data, index=symbol )
df.name='美股'
df.index.name = '代号'
haveLine(df)
print(df)
