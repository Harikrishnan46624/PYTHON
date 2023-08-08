import numpy as np

# arr1 = np.array([1,2,3,4,5,6])
# print(arr1.dtype)

# arr2 = np.array([1.1,2.6,3.4,4,5,6])
# print(arr2.dtype)

a = np.arange(6)
a2 = a[np.newaxis, :]
print(a2.shape)
