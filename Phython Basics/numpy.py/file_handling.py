import numpy as np
import pandas as pd

# a = np.array([1, 2, 3, 4, 5, 6])
# # np.save('just_numpy', a)  #You can save it as “filename.npy” with:
# b = np.load('just_numpy.npy')
# print(b)


# csv_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# # np.savetxt('file_numpy.csv', csv_arr)  #You can save a NumPy array as a plain text file like a .csv or .txt file with
# a = np.loadtxt('file_numpy.csv')
# print(a)


# x = pd.read_csv("Book1.csv", header=0).values
# print(x)

# x = pd.read_csv("Book1.csv", usecols=['Artist', 'Plays']).values
# print(x)

a = np.array([[-2.58289208,  0.43014843, -1.24082018, 1.59572603],
              [ 0.99027828, 1.17150989,  0.94125714, -0.14692469],
              [ 0.76989341,  0.81299683, -0.95068423, 0.11769564],
              [ 0.20484034,  0.34784527,  1.96979195, 0.51992837]])

df = pd.DataFrame(a)
# print(df)
# df.to_csv('array.csv')
# data = pd.read_csv('array.csv')
# print(data)

np.savetxt('array.csv', a, fmt='%.2f', delimiter=',', header='1,  2,  3,  4')
data = pd.read_csv('array.csv')
print(data)