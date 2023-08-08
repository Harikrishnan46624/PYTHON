import numpy as np


a = np.array([1, 2, 3, 0,0])
print(np.zeros(2))

print(np.ones(2))

# print(np.empty(4))

# print(np.arange(5))

p = np.linspace(0, 10, num=5)
print(p)

# x = np.ones(2, dtype=np.int64)
# print(x)

# arr1 = np.array([2, 1, 5, 3, 7, 4, 6, 8])
# x = np.sort(arr1)
# print(x)

# arr1 = np.array([2, 1, 5, 3]) 
# arr2 = np.array([ 7, 4, 6, 8])
# x = np.concatenate((arr1, arr2))
# print(x)

# x = np.array([[1, 2], [3, 4]])
# y = np.array([[5, 6]])
# a = np.concatenate((x,y),axis=0)
# print(a)

# arr1 = np.array([2, 1, 5, 3]) 
# print(arr1[0:2])
# print(arr1[-2:])

a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(a[a < 5]) #print all of the values in the array that are less than 5.
# print(a[a >= 5])
# print(a[a%2 == 0])
# c = a[(a > 2) & (a < 11)]
# print(c)
b = np.nonzero(a < 5)
print(b)
