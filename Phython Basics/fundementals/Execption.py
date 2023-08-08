a = 10
b = 0
try:
    print(a/b)
    print('try completed')
except ZeroDivisionError:
    print("Cant divide by zero")
except Exception:
    print("Something wrong")
finally:
    print("programme completed")