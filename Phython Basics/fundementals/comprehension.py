# tuple1 = ('mom', 'ant', 'malayalam', 'bat')
# list_pal = []
# for i in tuple1:
#     if i == i[::-1]:
#         list_pal.append(i)
# print(list_pal)


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

# nums = [1,2,3,4,5,6,7]
# my_list = []
# for n in nums:
#     my_list.append(n)
# print (my_list)

# nums = [1,2,3,4,5,6,7]
# my_list = [n for n in nums]
# print (my_list)

# nums = [1,2,3,4,5,6,7]
# my_list = [n*n for n in nums]
# print(my_list)

# nums = [1,2,3,4,5,6,7]
# my_list = [n for n in nums if n%2 == 0]
# print(my_list)


# my_list = []
# for letter in 'abcd':
#     for num in range(5):
#         my_list.append((letter, num))
# print(my_list)

# my_list = [(letter, num) for letter in 'abcd' for num in range(5)]
# print(my_list)

# names = ['Bruce', 'Clarak', 'peter', 'Logan']
# heros = ['Batman', 'Superman', 'Spider man', 'Deadpool']
# my_dict = {}
# for x,y in zip(names,heros):
#     my_dict[x] = y
# print(my_dict)

# names = ['Bruce', 'Clarak', 'peter', 'Logan']
# heros = ['Batman', 'Superman', 'Spider man', 'Deadpool']
# my_dict = {x: y for x,y in zip(names,heros)}
# print(my_dict)

# nums = [1,1,1,2,2,3,3,4,5,6,7]
# m = {n for n in nums}
# print(m)

# nums = [1,2,3,4,5,6,7]
# def gen_func(nums):
#     for n in nums:
#         yield n*n
# my = gen_func(nums)
# for i in my:
#     print(i)

# nums = [1,2,3,4,5,6,7]

# my = (n*n for n in nums)
# print(my)


# list1 = []
# n = 3
# for i in range(n):
#     i = int(input('enter '))
#     list1.append(i)
# print(list1)

# nums = 6
# fact = 1
# for i in range(1,nums+1):
#     fact = fact * i
# print(fact)

# list1 = []
# n = int(input("Enter the limit"))
# for i in range(n):
#     l = int(input("ENter the elemets"))
#     list1.append(l)
# print(list1)


# list1 = [1,2,3,4,5,6,7]
# list2 = [i for i in list1 if i%2 == 0]
# print(list2)