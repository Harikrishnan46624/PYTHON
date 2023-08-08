# pos = -1
# def search(list1, n):
#     l = 0
#     u = len(list1) - 1
#     while l <= u:
#         mid = (l + u) // 2
#         if list1[mid] == n:
#             globals()['pos'] = mid
#             return True
#         else:
#             if list1[mid] < n:
#                 l = mid + 1
#             else:
#                 u = mid - 1
#     return False

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n = 3
# if search(list1, n):
#     print('Found at', pos+1)
# else:
#     print('Not found')


def binary_search(num,key):
    start = 0
    end = len(num) - 1
    while start <= end:
        mid = (start + end) // 2
        if num[mid] == key:
            return mid+1
        elif num[mid] < key:
            start = mid + 1
        elif num[mid] > key:
            end = mid - 1
    return -1
pos = binary_search([10,20,30,40,50],20)
if pos!= -1:
    print("Found the value at position",pos)
else:
    print("not found")


# def search(list1,key):
#     low = 0
#     end= len(list1)-1
#     found = False
#     while low <= end and not found:
#         mid = (low + end) // 2
#         if key == list1[mid]:
#             found = True
#         elif key > list1[mid]:
#             low = mid + 1
#         else:
#             end = mid -1 
#     if found == True:
#         print("Key is found")
#     else:
#         print("Key not Found")
# list1 = [10,20,30,40,50,6,0,70,80]
# list1.sort()
# key = 40
# search(list1,key)

# def binary_search(nums,target):
#     start = 0
#     end = len(nums) - 1
#     while start <= end:
#         mid = (start + end) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return -1