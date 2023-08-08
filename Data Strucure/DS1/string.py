# def replace_alphabet(string, n):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     result = ''

#     for char in string:
#         if char.isalpha():
#             if char.islower():
#                 index = (alphabet.index(char) + n) % 26
#                 result += alphabet[index]
#             else:
#                 char = char.lower()
#                 index = (alphabet.index(char) + n) % 26
#                 result += alphabet[index].upper()
#         else:
#             result += char

#     return result


# input_string = "Hello, World!"
# n_value = 3
# output_string = replace_alphabet(input_string, n_value)
# print(output_string)


# def palindrome(str):
#     str = str.replace(" ","").lower()
#     return str == str[::-1]
# input_str = input("Enter a string: ")
# if palindrome(input_str):
#     print("The string is palindrome")
# else:
#     print("Not palindrome")



# def compress_string(string):
#     compressed = ""
#     count = 1
    
#     for i in range(1, len(string)):
#         if string[i] == string[i - 1]:
#             count += 1
#         else:
#             compressed += string[i - 1] + str(count)
#             count = 1
    
#     # Add the last character and its count
#     compressed += string[-1] + str(count)
    
#     # Return the compressed string if it is shorter than the original
#     return compressed if len(compressed) < len(string) else string

# # Test the function
# input_string = input("Enter a string: ")
# compressed_string = compress_string(input_string)
# print("Compressed string:", compressed_string)


# def replace(str,n):
#     result = ''
#     for char in str:
#         if char.isalpha():
#             ascii = ord(char)
#             base = ord('a') if char.islower() else ord('A')
#             new_char = chr((ascii - base + n)%26 + base)
#             result += new_char
#         else:
#             result += char
#     return result
# input_string = input("Enter a string: ")
# shift_value = int(input("Enter the shift value: "))

# modified_string = replace(input_string, shift_value)
# print("Modified string:", modified_string)


# def avg (list1):
#     prime = 0
#     even = 0
#     count = 0
#     even_count = 0
#     for num in list1:
#         if num%2 != 0:
#             prime += num
#             count += 1
#         if num%2 == 0:
#             even += num
#             even_count += 1
#     avg_prime = prime / count
#     avg_even = even / even_count
#     print(avg_prime)
#     print(avg_even)
# avg([10,12,11,44,32])
# 
# import math
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True

# def average_prime_and_nonprime(numbers):
#     prime_sum = 0
#     nonprime_sum = 0
#     prime_count = 0
#     nonprime_count = 0

#     for num in numbers:
#         if is_prime(num):
#             prime_sum += num
#             prime_count += 1
#         else:
#             nonprime_sum += num
#             nonprime_count += 1

#     average_prime = prime_sum / prime_count if prime_count > 0 else 0
#     average_nonprime = nonprime_sum / nonprime_count if nonprime_count > 0 else 0

#     return average_prime, average_nonprime

# # Example usage:
# numbers = [2, 3, 5, 8, 10, 12, 15]
# average_prime, average_nonprime = average_prime_and_nonprime(numbers)
# print("Average of prime numbers:", average_prime)
# print("Average of non-prime numbers:", average_nonprime)


# str1 = input("Enter the string: ")
# rev = str1[::-1]
# if str1 == rev:
#     print("palindrome")
# else:
#     print("Not palindrome")

numbers = [2,2, 3, 5, 8, 10, 12, 30 , 15]
n = len(numbers)
for i in range(n):
    count = 0
    for j in range(n):
        if i != j and numbers[i] == numbers[j]:
            numbers[i]
            count += 1
    if count == 0:
        print(numbers[i])
        break
            