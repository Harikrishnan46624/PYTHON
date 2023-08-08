from array import *
arr1  = array('i',[])
n = int(input("Enter the length: "))
for i in range(n):
    x = int(input("Enter the values {}: ".format(i+1)))
    arr1.append(x)

print(arr1)
arr2 = arr1
arr2.append(70)
arr2.append(80)
print(arr2)
