def getArray():
    global arr
    arr = []
    n = int(input("Enter the size of array: "))
    for i  in range(n):
        num = int(input("Enter the number: "))
        arr.append(num)
def displayArray():
    print("Array elements ar: ")
    for i in arr:
        print(i)
def main():
    getArray()
    displayArray()
if __name__ == "__main__":
    main()