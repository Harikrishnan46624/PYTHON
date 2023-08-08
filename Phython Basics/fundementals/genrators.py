# def fib(mymax):
#     a,b = 0, 1
#     while True:
#         c = a+b
#         if c < mymax:
#             print("before")
#             yield c
#             print("after")
#             a = b 
#             b = c
#         else:
#             break
# y = fib(10)
# print(next(y))

def gen1():
    yield 10
    yield 20
    yield 30
    yield 40
    yield 50
x = gen1()
print(next(x))
print(next(x))
# # print(next(x))
# # print(next(x))
# # print(next(x))


# def gen2():
#     for i in range(1, 11):
#         yield i
# y = gen2()
# print(next(y))
# print(next(y))

# def Top():
#     n = 1
#     while n <= 10:
#         sq = n * n
#         yield sq
#         n += 1
# val = Top()

# for i in val:
#     print(i)
