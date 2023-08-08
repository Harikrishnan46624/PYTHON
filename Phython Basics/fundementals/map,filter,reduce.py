def sqr_root(n):
    return n**(1/2)
s = sqr_root(9)
print(s)

# map
# map syntax- map(function_name,itrable)
sqr_root = lambda nums:nums**(1/2) 
nums = [10,20,30,55,44,9,14,17]
s = map(sqr_root, nums)
d = list(s)
print(d)

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared) 


filter
nums = [10,20,30,55,44,9,14,17]
odd = lambda nums: nums%2 == 0
s = filter(odd,nums)
d = list(s)
print(d)

items = [1, 2, 3, 4, 5]
even_nums = list(filter(lambda x: x % 2 == 0, items))
print(even_nums) 


reduce
from functools import reduce
nums = [10,20,30,40]
add = lambda  x,y: x + y 
s = reduce(add,nums)
print(s)

from functools import reduce
items = [1, 2, 3, 4, 5]
sum_of_items = reduce(lambda x, y: x + y, items)
print(sum_of_items) 
