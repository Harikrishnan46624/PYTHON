def palin(s):
    left=0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left +=1
        right -=1
    return True

s = input("Enter a string: ")
if palin(s):
    print(format(s)," is a palindrome")
else:
    print(format(s),"is not a palindrome",)
    