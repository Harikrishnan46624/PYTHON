
def insertion(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr)
       

arr = [64, 34, 2, 8]
insertion(arr)
# print(arr)

