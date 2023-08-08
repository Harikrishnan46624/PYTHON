def selection(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:     
                arr[i], arr[j] = arr[j], arr[i]
        print(arr)

arr = [7, 2, 4, 1, 5, 3]
selection(arr)
# print(arr)


# arr = [7, 2, 4, 1, 5, 3]
# for i in range(len(arr)):
#         min_index = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#         print(arr)