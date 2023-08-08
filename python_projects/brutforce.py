from string import*
from itertools import product

value = ascii_letters + digits + punctuation
print(value)
for i in range(1,5):
    for j in product(value,repeat=i):
        word = "".join()
        p = open("password.txt","a")
        p.write(word)
        p.write("\n")

