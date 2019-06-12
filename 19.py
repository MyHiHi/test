import scipy.integrate as sci
import datetime
import time
import pandas as pd
import scipy.interpolate as spi
import scipy as sp
import os
import numpy as np


def pr(*args):
    os.system('cls')
    for i in args:
        print(i, '\n', '----------------')


arr = np.random.randint(1, 10, size=(3, 2, 2, 2))

# pr(arr,arr.mean(axis=1))

arr = np.random.randint(1, 10, size=(4, 2))

# pr(arr,arr.sum(axis=1))
b1 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])

# pr(b1.ndim)

a = np.array([[[1, 2, 3], [4, 5, 6]]])
b1 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
b2 = np.arange(3).reshape((1, 3))
b3 = np.arange(6).reshape((2, 3))
b4 = np.arange(12).reshape((2, 2, 3))
b5 = np.arange(6).reshape((2, 1, 3))

# pr(a,b5,a+b5)


# x=np.random.randint(1,10,size=(2,2))
x = np.linspace(-2*np.pi, 2*np.pi, 11)


def f(x): return np.sin(x)+0.5*x


c = f(x)
# pr(c,x.shape)
tck = spi.splrep(x, c, k=1)
# pr(x,c,tck,len(tck))
iy = spi.splev(x, tck)


def paint(x, y, iy):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(8, 4), dpi=80)
    plt.plot(x, y, color='blue', linewidth=3.5, label='true value')
    plt.scatter(x, iy, 30, color='red', label='interpolate value')

    plt.legend(loc=0)

    plt.grid(True)

    plt.xlabel('x')

    plt.ylabel('y(x)')

    plt.show()


x = np.linspace(1.0, 3.0, 50)


def f(x): return np.sin(x)+0.5*x


c = f(x)
# pr(c,x.shape)
tck = spi.splrep(x, c, k=1)

iy = spi.splev(x, tck)

# paint(x,c,iy)


p = pd.read_excel(r'C:\Users\Administrator\Desktop\财产损失明细表.xls')
# pr(p)
timestamp_now = time.strftime('%Y-%m-%d', time.localtime())
today = pd.Timestamp(timestamp_now)
# pr(timestamp_now,today)

start = datetime.datetime.strptime('2019-08-05', '%Y-%m-%d')
end = datetime.datetime.strptime('2019-11-05', '%Y-%m-%d')
d_s = (start - today).days
d_e = (end - today).days
# pr(d_s,d_e,type(today),type(d_s))


f= lambda x: np.sin(x)+0.5*x


a = 0.5
b = 9.5
vi = sci.fixed_quad(f, a, b)
vi=sci.quad(f,a,b)
vi=sci.romberg(f,a,b)
# pr(vi)


from scipy.stats import norm

def bscall(S0,K,r,T,sigma):
    d1=np.log(S0*np.exp(r*T)/K)/(sigma*np.sqrt(T))+(sigma*np.sqrt(T))/2
    d2=np.log(S0*np.exp(r*T)/K)/(sigma*np.sqrt(T))-(sigma*np.sqrt(T))/2
    c=S0*norm.cdf(d1)-np.exp(-r*T)*K*norm.cdf(d2)
    return c;

(S0, K, r, T, sigma) = (100, 95, 0.05, 1, 0.1)
c=bscall( S0, K, r, T, sigma )
pr(c,float('-inf'))