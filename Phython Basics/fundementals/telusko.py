#List
# nums = [25, 36, 72, 95 ,62]
# nums.append(20)
# nums.insert(3,90)
# nums.pop(1)
# nums.remove(95)
# nums.extend([30, 62])
#print(sum.nums)
# print(nums)

#Tuple
# tup = (21, 66, 72 ,89)
# print(tup[1])
# print(tup)

# set
# s = {22,36,66,78,99,100}
# print(s)

#dictinory
# data = {1: 'dasan', 2: 'kiran', 3: 'hari'}
# print(data)
# print(data.get(3))
# keys = ['hari', 'sachin', 'raman']
# values = ['python', 'java', 'php']
# data = dict(zip(keys,values))
# print(data)
# print(data['hari'])
# del data['sachin']
# print(data)

# keys and values
# d = {'hari': 'poco', 'sachin': 'samsung', 'raman': 'apple'}
# print(d.keys())
# print(d.values())


# swping
# a = 5
# b = 10
# a,b = b,a

# print(a)

# import math
# x = math.sqrt(25)
# print(x)
# m = math.pow(3, 2)
# print(m)

#Eval
# result = eval(input("Enter here: "))
# print(result)

#While loop
# i = 1
# while i <= 5:
#     print("Flynn", i)
#     i = i+1

# for i in range(1, 101):
#     if i%3 == 0 or i%5 == 0:
#         continue
#     print(i)

# n = 4
# for i in range(n):
#     for j in range(n-i):
#         print("#",end=" ")
#     print()    

# nums = [1,2,3,4,5,6,7]
# for i in nums:
#     if i%5 == 0:
#         break
#     print (i)


# from array import *
# vals = array('i',[1, 2, 3, 4, 5, 6 ,7])
# for i in vals:
#  print(i)

# from array import *
# arr  = array('i',[])
# n = int(input("Enter the length: "))
# for i in range(n):
#     x = int(input("Enter the values{}: ".format(i+1)))
#     arr.append(x)
# print(arr)
# val = int(input("Enter the value to search: "))
# k=0
# for e in arr:
#     if e == val:
#         print(k+1)
#         break
#     k += 1

# from numpy import *
# arr = linspace(0,15,20)
# print(arr.dtype)
# print(arr)

# from numpy import *
# arr1 = array([
#     [10,20,30],
#     [40,50,60]
#               ])
# arr2 = arr1.flatten()
# print(arr1)
# print(arr2)

#Functions
# def greet():
#     print("Hello")
# def add(x, y):
#     c = x + y
#     d = x - y
#     return c,d
# result1,result2 = add(5, 4)
# print(result1, result2)
# greet()

# def update(x):
#     x =8
#     print(x)
# update(10)

# def person(name,age):
#     print(name)
#     print(age)
# person(name='navin',age=20)

# def sum( *b):
#     c = 0
#     for i in b:
#         c = c + i
#     print(c)
# sum(5,6,7,8)


# a = 10
# print(id(a))
# def some():
#     a = 9
#     x = globals()['a']
#     print(id(x))

# some()

# def count(lst):
#     even = 0
#     odd = 0
#     for i in lst:
#         if i%2 == 0:
#             even += 1
#         else:
#             odd +=1
#     return even,odd
# lst = [10,20,30,55,44,66,21,33,77,5]
# even,odd = count(lst)
# print('Even : {} and odd : {}'.format(even,odd))


# def fib(n):
#     a = 0
#     b = 1
    
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c = a + b
#         a = b
#         b = c
#         print(a + b)

# fib(10)

# def fact(n):
#     f = 1
#     for i in range(1, n+1):
#         f = f * i
#     return f
# x = 5
# result = fact(x)
# print(result)


# Recursion
# import sys
# print(sys.getrecursionlimit())
# def greet():
#     print('hello')
#     greet()


# def fact(n):
#     if n == 0:
#         return 1
    
#     return n *fact(n-1)

# result = fact(5)
# print(result)


# numbers = [10, 5, 20, 15, 25]
# numbers.sort(reverse=True)
# second_largest = numbers[1]
# print(second_largest)

#Lambada
# nums = [1,2,3,4,5,6,7]
# even = list(filter(lambda n : n%2 == 0,nums))
# print(even)

#Decorator
# def div(a,b):
#     print(a/b)

# def smart_div(func):
#     def inner(a,b):
#         if a < b:
#             a,b = b,a
#             return func(a, b)
#     return inner
# div = smart_div(div)
# div(2,4)
# class Book:


#     def __init__ (self,name,pages):
#         self.name = name
#         self.pages = pages
#         print(name, pages)
# book1 = Book("python", 900)
# book1.name
# book1.pages



# i = 1
# while i <= 10:
#     print('python')
#     i +=1
# print('completed')


# def add(a,b):
#     c = a + b
#     return c
# a1 = add(5, 4)
# print(a1)

# def values(*n):
#     s = 0
#     for i in n:
#         print(i)
# values(1,23,6,5,1,90)

 
# def values(*n):
#     s = 0
#     for i in n:
#         s += i 
#     return s
# val1 = values(1,23,6,5,1,90)
# print(val1)

# def function(**x):
#     print(x)
#     print(type(x))
# function(num1 =10, num2 = 20,num3 = 30)

# p = lambda a,b : a if a < b else b
# s = p(5,10)
# print(s)

# a = 10
# def value():
#     global a
#     print(a)
# value()

#eval
# s1 = '55'
# s2 = '53.3'
# s3 = '[1,2,3,4]'
# s4 = '{"a" = "g","b" = "k","c" = "m"}'
# s3_new = eval(s3)
# print(type(s3_new))


# a = 100
# b = 200
# a,b = b,a
# print(a)

# fibonacci
# i = 1
# n  = int(input("Enter the number"))
# a, b = 1, 2

# while i <= n:
#     print(a)
#     a,b = b, a+b
#     i += 1

# List Comprehsion
# tuple1 = ('mom', 'ant', 'malayalam', 'bat')
# list_pal = []
# for i in tuple1:
#     if i == i[::-1]:
#         list_pal.append(i)
# print(list_pal)
#

# tuple1 = ('mom', 'ant', 'malayalam', 'bat')
# a = [i for i in tuple1 if i == i[::-1]]
# print(a)


# numers = [10, 20, 30, 40]
# a = [i/2 for i in numers]
# print(a)

# value1 = list(range(1, 11))
# print(f"values:{value1}")
# even  = [i for i in value1 if i%2 == 0]
# squre = [i**2 for i in value1 if i%2 == 0]
# print(even)
# print(squre)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# a = [i for i in fruits if "a" in i]
# print(a)

# import time
# start = time.time()
# print(start)
# list1 = []
# for i in range(500000):
#     list1.append(i)

# stop = time.time()
# stop = time.time()
# time_taken = stop - start
# print(time_taken)                                                               

# import time
# print('python')
# time.sleep(5)
# print('python is simple')

# S = input("Enter the string: ")
# a = ""
# for i in S:
#     if i not in a:
#         a += i
# print(len(a))
# d = [i for i in S if i not in a]
# print(len(d))

# from copy import *
# nums1 = [[1,2,3,4],[5,6,7]]
# nums2 = deepcopy(nums1)
# print("second",nums2)
# nums1[1][0] = 10
# print("second",nums2)
# print("first",nums1)

# arr = [10,20,55,44]
# for i in range(0,len(arr)):
#     if arr[i]%2 == 0:
#         arr[i]
# for j in range(0,len(arr)):
#     if arr[j] %2 != 0:
#         arr[j]

# #min value
# list1 = [1,2,-8,7,12,4]
# max = list1[0]
# for i in list1:
#     if i < max:
#         max = i
# print(max)

# # string
# list1 = ['abc', 'xyz', 'aba', '1221']
# ctr = 0
# for i in list1:
#     if len(i) > 1 and i[0] == i[-1]:
#         ctr += 1
# print(ctr)

## unique
# list1 = [4,1,2,-8,7,12,4,1,4]
# uniq = []
# for i in list1:
#     if i not in uniq:
#         uniq.append(i)
# print(uniq)
# for x in uniq:
#       print(x)


# list1 = [4,1,2,-8,7,12,4,1,4]
# list2 = list(list1)
# print(list2)

# str1 = "The quick brown fox jumps over the lazy dog"
# n = 3
# word = []
# txt = str1.split(" ")
# for i in txt:
#     if len(i) > n:
#         word.append(i)
# print(word)

##check same numbers in two lists
# list1 = [4,1,2,-8,7,12,4,1,4]
# list2 = [5,12,24,32]
# result = False
# for i in list1:
#     for j in list2:
#         if i == j:
#             result = True
# print(result)


# #list after removing the 0th, 4th and 5th element
# list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# list2 = []
# # list1 = [x for (i,x) in enumerate(list1) if i not in (0,4,5)]
# for i,x in enumerate(list1):
#     if i not in (0, 4, 5):
#         list2.append(x)
# print(list2)


## 3*4*6 3D array whose each element is *
# arr = []
# # array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
# for row in range(3):
#     row_inn = []
#     for col1 in range(4):
#         col1_inn = []
#         for col2 in range(6):
#             col1_inn.append('*')
#         row_inn.append(col1_inn)
#     arr.append(row_inn)
# print(arr)


##removing even numbers from it.
# list1 = [4,1,2,-8,7,12,4,1,4]
# # list1 = [i for i in list1 if i%2 == 0]
# list2 = []
# for i in list1:
#     if i%2 == 0:
#         list2.append(i)
# print(list2)


##program to shuffle and print a specified list
# from random import shuffle
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# shuffle(color)
# print(color)

## print the numbers of a specified list after removing even numbers from it.
# list1 = [4,1,2,-8,7,12,4,1,4]
# list1 = [i for i in list1 if i%2 != 0]
# print(list1)


##list of the first and last 5 elements where the values are square numbers between 1 and 30
# l = list()
# for i in range(1,21):
#     l.append(i ** 2)
# print(l[:5])
# print(l[-5:])


## check if each number is prime in a given list of numbers
# list1 = [0, 3, 4, 7, 9]
# result = []
# for n in list1:
#     if (n == 1):
#         result.append(False)
#     elif (n == 2):
#         result.append(True)
#     else:
#         prime = True
#         for x in range(2,n):
#             if(n%x == 0):
#                 prime = False
#                 break
#         result.append(prime)

# print(result)


##to generate all permutations
# import itertools 
# print(list(itertools.permutations([1,2,3])))


##calculate the difference between the two lists.
# list1 = [1, 3, 5, 7, 9]
# list2 = [1, 2, 4, 6, 7, 8]
# diff1 = list(set(list1) - set(list2))
# diff2 = list(set(list2) - set(list1))
# total = diff2 + diff1
# print(total)


##program to access the index of a lis
# list1 = [1, 3, 5, 7, 9]
# dict1 = {}
# for key,value in enumerate(list1):
#     dict1[key] =  value
#     # dict1[value] = value
# print(dict1)


# list1 = [4,-8,7,12,4,1,4]
# n = len(list1)
# for i in range(n):
#     count = 0
#     for j in range(n):
#         if i != j and list1[i] == list1[j]:
#             list1[i]
#             count += 1
#     if count == 0:
#         print(list1[i])
#         break

# list1 = [4,-8,7,12,4,1,4]
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)