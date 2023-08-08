from numpy import*
matrix1 = []
matrix2 = []
matrix3 = []
n = int(input('number of rows: '))
print("values of array1")
for i in range(n):
    a = []
    for j in range(n):
        l = int(input())
        a.append(l)
        matrix1.append(a)

print("values of array2")
for i1 in range(n):
    a = []
    for j1 in range(n):
        l1 = int(input())
        a.append(l1)
        matrix2.append(a)
print(matrix1)
print(matrix2)

# for i2 in range(n):
#     res = []
#     for j2 in range(n):
#         r = matrix1[i][j] + matrix2[i1][j1]
#         res.append(r)
#     matrix3.append(res)
# print(matrix3)