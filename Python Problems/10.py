def sort_des(arr):
    n = len(arr)
    for i in range (n):
        for j in range (0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j],  arr[j+1] = arr[j+1], arr[j]
    return arr

n = int(input("Enter the Size of Array: "))
arr = []
for i in range(n):
    num = int(input("Enter the element {}: ".format(i+1)))
    arr.append(num)
    sorted  = sort_des(arr)
print("Sorted values: ",sorted)
