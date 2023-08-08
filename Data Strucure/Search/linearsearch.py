# def search(list1,n):
#     i = 0
#     while i < len(list1):
        
#         if list1[i] == n:
#             return True
#         i = i + 1
#     return False
# list1 = [1,2,3,4,5,6,9]
# n  = 9
# if search(list1, n):
#     print('Found')
# else:
#     print('not found')


def linear(list1,key):
    flag = False
    for i in range(0,len(list1)):
        if list1[i] == key:
            flag = True
            found = i
    if flag == True:
        print(found+1)
    else:
        print('key not found')
list1 = [10,7,4,1,19,23,100]
key = 7
linear(list1,key)