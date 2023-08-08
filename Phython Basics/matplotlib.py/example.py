import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# fig, ax = plt.subplots()
# ax.plot([1,2,3,4], [1,4,2,3])
# # plt.show()

# fig = plt.figure() # an empty figure with no Axes
# fig, ax = plt.subplots() # a figure with a single Axes
# fig, ax = plt.subplots(2, 2) # a figure with a 2x2 grid of Axes
# # a figure with one axes on the left, and two on the right:
# fig, axs = plt.subplots([['left', 'right-top'],
#                          ['left', 'right-bottom']])



# np.random.seed(19680801)
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100

# fig, ax = plt.subplots(figsize=(7, 5))
# ax.scatter('a', 'b', c='c', s='d', data=data)
# ax.set_xlabel('entry a')
# ax.set_ylabel('entry b')
# plt.show()


# x = np.linspace(0, 2, 100)
# fig, ax = plt.subplots(figsize = (5, 2.7), layout = 'constrained')
# ax.plot(x, x, label='linear')
# ax.plot(x, x**2, label='quadratic')
# ax.plot(x, x**3, label='cubic')
# ax.set_xlabel('x label')
# ax.set_ylabel('y label')
# ax.set_title("simple plot")
# ax.legend()
# plt.show()




# def my_plotter(ax, data1, data2, style):
#     ax.plot(data1, data2, **style)

# data1, data2, data3, data4 = np.random.randn(4, 100)  # make 4 random data sets

# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
# my_plotter(ax1, data1, data2, {'marker': 'x'})
# my_plotter(ax2, data3, data4, {'marker': 'o'})

# fig, ax = plt.subplots(figsize=(5, 2.7))
# x = np.arange(len(data1))
# ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--')
# ax.plot(x, np.cumsum(data2), color='orange', linewidth=2, linestyle=':')

# plt.show()
