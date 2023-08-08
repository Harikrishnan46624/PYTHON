# def buble(arr):
#     n = len(arr)
#     swapped = False
#     for i in range(n-1):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j + 1]:
#                 swapped = True
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#         if not swapped:
#             return
# arr = [10,12,46,5,9,32,44,98]
# buble(arr)

# for i in range(len(arr)):
#     print("%d" % arr[i], end=" ")


# arr = [10,12,46,5,9,32,44,98,32]
# n = len(arr)
# for i in range(n):
#     for j in range(0, n - i -1):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             print(arr)


# def buble(arr):
#     count = 0
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n - i -1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#             count += 1
#         if not swapped:
#             break
#     return count,arr

# print(buble([10,12,46,5,9,32,44,98]))



def buble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(arr)
            

arr = [7, 2, 4, 1, 5, 3]
buble(arr)
# print("sorted array: ", arr)