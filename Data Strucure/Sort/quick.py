def quick(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        low = [x for x in arr if x < pivot]
        equal = [x for x  in arr if x == pivot]
        high = [x for x  in arr if x > pivot]
        print(quick(low) , equal ,quick(high))
        
        return quick(low) + equal + quick(high)

arr = [70, 24, 2, 4, 1, 5, 3, 12]
sort = quick(arr)
print(sort)






