# list1 = [1, 3, 5, 3, 7, 9]
# count = 0
# for i in list1:
#     if i == 3:
#         count += 1
# print(count)


# def dup(list1):
#     set1 = set()
#     duplicate = -1
#     for i in range(len(list1)):
#         if list1[i] in set1:
#             return list1[i]
#         else:
#             set1.add(list1[i])
#     return duplicate
# print(dup([1, 3, 5, 3, 7, 9]))


# def max_pro(list1):
#     list1_len = len(list1)
#     if list1_len < 2:
#         print("no pairs")
#         return
#     x = list1[0]
#     y = list1[1]
#     for i in range(0, list1_len):
#         for j in range(i+1, len(list1)):
#             if (list1[i] * list1[j] > x * y):
#                 x = list1[i]
#                 y = list1[j]

#     return x, y
# print(max_pro([1, 3, 5, 3, 7, 9]))

# list1 = [1, 3, 5, 3, 7, 9]
# list12 = []
# for i in list1:
#     for j in range(i+1,len(list1)):
#         if list1[i] == list1[j]:
#             list12.append(list1[i])
# print(list12)

# def test(list1):
#     return sum(range(10,21)) - sum(list(list1))
# list1 = [10, 11, 12, 13, 14, 16, 17, 18, 19, 20]   
# for i in range(len(list1)):
#     print(list1[i], end=" ")
# print("\nmissing number",test(list1))



# list1 = [10, 11, 12, 13, 14, 16, 17, 18, 19, 20] 
# n = len(list1)
# for i in range(0,n):
#     for j in range(i+1,n):
#         if list1[i] > list1[j]:
#             temp = list1[i]
#             list1[i] = list1[j]
#             list1[j] = temp
# print(list1[-2])


arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
n = len(arr)
count = 0
for i in range(n):
    if arr[i] != 0:
        arr[count] = arr[i]
        count += 1
        # print(arr)
        # print(count)
while count < n:
        arr[count] = 0
        count += 1
print(arr)