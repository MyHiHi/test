# p=[[12,23,4,5,6,33,4,5,345],[12,44,444,2],[12,44,444,2],[12,44,444,2]]
# from functools import reduce

# c=reduce(lambda x,y:x+y,[len(i) for i in p])
# print(c)
# import decimal
# from decimal import Decimal

# decimal.getcontext().prec=5
# c=Decimal(1)/Decimal(3)
# print(c,len(str(c))-2)

import os

import numpy as np

languages = ['Python', 'R', ['Matlab', 'C++']]
a, *p = languages
# print(p)
# def pr (nt,*args):
#     for i in args:
#         print(i)
# pr(2,*languages)


# tree=lambda c: [y for x in c for y in tree(x)] if isinstance(c,list) else [c]

# print(tree([1,2,[23,3],[[22,35,5],[99]]]))


arr = numpy.array([[1, 2, 3], [4, 5, 7]])

arr = numpy.arange(15)
arr = arr.reshape((1, 3, 5))
arr = numpy.linspace(2, 6, 3)
# print(arr)
# print(numpy.random.random((2,3,4)))
# print(numpy.eye(4,k=-1,dtype=int))
# print(numpy.ones(4,dtype=int))

# c=numpy.array([12,2,45,56,5,6],dtype=int).reshape((3,2,1))
# print(c)
# print(type(c))
# print(c.ndim,c.size,c.shape)
# print(len(c),c.dtype,c.strides)
# print(len([12,2,2,[3,4,5,[5,56]]]))

p = numpy.random.random((2, 3))
# numpy.save(file='d:\\arr_p',arr=p)
# import time
# time.sleep(10)
# print(numpy.load(file='d:\\arr_p.npy'))

# numpy.savetxt('d:\\arr_p2.csv',p)

# print(numpy.genfromtxt('d:\\arr_p2.csv'))

arr = [[12, 2, 3], [45, 5, 6], [66, 53, 4]]
arr = numpy.array(arr)
# print(arr)
# print(arr[2:,[0,2]])
# print(arr[1,:2])
# print(arr.T[:,[0,1]])
code = np.array(['BABA', 'FB', 'JD', 'BABA', 'JD', 'FB'])

# print(code=='BABA')

price = np.array([[170, 177, 169], [150, 159, 153],
                  [24, 27, 26], [165, 170, 167],
                  [22, 23, 20], [155, 116, 157]])

# price[price<34]=0

# arr=np.arange(14)
# print(arr)

# price=price.ravel(order='F')
# arr=price.ravel(order='c')
os.system('cls')
arr = price.flatten(order='f')
# arr[0]=1000
arr1 = arr.reshape((-1, 6), order='f')
# print(arr)
# print('---------------')
# print(arr1)


def pr(*args):
    os.system('cls')
    for i in args:
        print(i, '\n', '----------------')


arr1 = np.arange(12).reshape((3, 4))
arr2 = np.arange(13, 25).reshape((3, 4))
arr3 = np.concatenate([arr1, arr2],)
arr3 = np.hstack((arr1, arr2))
arr3 = np.vstack((arr1, arr2))
# pr(arr1,arr2,arr3)

arr4 = np.r_['r', [1, 2, 3], [4]]
# pr(arr4,type(arr4))

first, second = np.vsplit(arr3, [2])
arr6 = np.hsplit(arr3, [1, 3])
# pr(arr3,first,second)

arr7 = arr3.repeat([1, 2, 3, 4], axis=1)
arr7[:, 1] = np.arange(6)
# pr(arr7)
arr7 = numpy.repeat(arr3, [1, 2, 3, 4], axis=1)
arr7 = np.tile(arr3, (1, 1, 3))
# pr(arr7)

arr8 = np.random.randint(20, size=(3, 4))
# pr(arr8)
# arr8.sort()
arr9 = np.sort(arr8, axis=0)
arr10 = np.sort(arr8, axis=1)
# pr(arr8,arr9,arr10)
arr11 = arr8[:, arr8[0].argsort()]
# pr(arr8,arr8[0].argsort(),arr11)
# arr12=np.insert(arr8,[1,2],122,axis=0)
arr12 = np.random.randint(12, 100, size=(3, 4))
# pr(arr8,arr12,arr8/arr12**2,arr8/(arr12**2))

arr2d = np.array([[1, 2], [3, 1]])

arrMat = np.asmatrix(arr2d)

# pr(arr2d,type(arr2d.transpose()) ,type(arr2d.T ),type(arrMat.transpose()))

# pr(np.linalg.inv(arr2d) * arrMat.I, arrMat**-1)

arr = np.array([3, 2])
# pr(arr , arr.T)
arrMat2 = np.asmatrix(arr).T
# pr(arr.T.shape,arrMat.T.shape)
# pr(arrMat,arrMat2,arrMat*arrMat2)
# pr(arr2d,arr,type(np.dot(arr2d,arr)))
# pr(arr,arrMat2,arr+arrMat2)
# pr(arr.shape,arrMat2.shape)
x = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
y = np.array([[3, 2, 1], [1, 1, 1]])
# pr(x.shape,y.shape)

x = np.ones(shape=(2, 3, 4))
y = np.array([1, 2, 3, 4])
z = np.dot(x, y)
pr(x, y, z, z.shape)
print(z.shape)
print(z)
