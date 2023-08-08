# # Decorator
# def smart_div(func):
#     def inner(a,b):
#         if a < b:
#             a,b = b,a
#             return func(a, b)
#     return inner
# def div(a,b):
#     print(a/b)

# div = smart_div(div)
# div(2,4)


# def func1():
#     print('python')
# a = func1
# a()

# def double(n):
#     return 2*n
# def add(a, b):
#     return a + b
# a = double(5)
# b = double(add(2, 3))
# print(a)
# print(b)

# def decorate(func):
#     def add (a, b):
#         result = func(a + b)
#         return result
#     return add

# @decorate
# def double(x):
#     return 2 * x

# @decorate
# def sq(x):
#     return x**2
# d = sq(5, 1)
# print(d)

# e = double(6, 7)
# print(e)

# def my_decorator(func):
#     def wrapper():
#         return "HELLO WORLD"
#     return wrapper

# @my_decorator

# def my_function():
#     pass

# result = my_function()
# print(result)



# def decor1(func):
# 	def inner():
# 		x = func()
# 		return x * x
# 	return inner

# def decor2(func):
# 	def inner():
# 		x = func()
# 		return 2 * x
# 	return inner

# @decor1
# @decor2
# def num1():
# 	return 10

# @decor2
# @decor1
# def num2():
# 	return 10

# print(num1())
# print(num2())


def decor(func):
    def add(a,b):
        result = func(a + b)
        return result
    return add

@decor
def sqr(x):
    return x ** 2

@decor
def sub(x):
    return x/2

print(sub(5,6))
print(sqr(5,6))
