# i = 1
# while i<=10 :
#     print(i)
#     i=i+1 
# else:
#     print("Loop finshed")

#find prime number and delete after two numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# # Given list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Find the prime number
# prime_number = None
# for num in numbers:
#     if is_prime(num):
#         prime_number = num
#         break

# # Delete two numbers
# if prime_number is not None:
#     prime_index = numbers.index(prime_number)
#     numbers.pop(prime_index)
#     if prime_index < len(numbers):
#         numbers.pop(prime_index)

# print("Prime number:", prime_number)
# print("Updated list after deletion:", numbers)

# list1 = [10,2,4,5,79,1,12]
# m = list1[0]
# for i in range(len(list1)):
#     if list1[i] < m:
#         m = list1[i]
# print(m)

# list1 = [10,2,4,5,79,1,12,2,4,5]
# num = []
# count = 0
# for i in list1:
#     if i not in num:
#         count += 1
#         num.append(i)
# print(count)
# print(num)

list1 = [1, 1, 1, 64, 23, 64, 22, 22, 22]
size = len(list1)
for i in range(size - 2):
    if list1[i] == list1[i + 1] and list1[i + 1] == list1[i + 2]:
        print(list1[i])