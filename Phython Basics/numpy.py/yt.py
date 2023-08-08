import numpy as np

# arr = np.array([1,2,3])
# print(type(arr))
# print(arr.ndim)
# print(arr.shape)
# print(arr.dtype)
# print(arr.itemsize)
# print(arr.size)

# arr = np.array([[1,2,3],[4,5,6]])
# print(arr.ndim)
# print(arr.shape)

# arr = np.array([[[1,2],[3,4]],[[4,5],[6,7]]])
# print(arr.shape)

# arr = np.array([[[1,2,3],[3,4,5]],[[4,5,6],[6,7,8]]])
# print(arr.shape)
# print(arr.itemsize)
# print(arr.size)

# arr = np.array([1 + 2.j, 9+ 6.j])
# print(arr.dtype)

arr = np.array([1,2,3],dtype= complex)
# print(arr)
# print(arr.imag)
# print(arr.real)
arr.imag = np.array([9,10,11])
print(arr)