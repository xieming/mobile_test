# __author__ = 'anderson'
#
# #encode='utf-8'
#
# from pylab import *
#
# # make a square figure and axes
# figure(1, figsize=(4,4))
# ax = axes([0.1, 0.1, 0.8, 0.8])
#
# fracs = [45, 30, 25]
# explode=(0, 0, 0.08)
# labels = 'Hogs', 'Dogs', 'Logs'
#
# pie(fracs, explode=explode, labels=labels,
#                 autopct='%1.1f%%', shadow=True, startangle=90, colors = ("g", "r", "y"))
#
#
# title('Raining Hogs and Dogs')
#
# show()

#coding=utf-8
# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3.5])
# plt.ylabel("hehe")
# plt.show()

# import matplotlib.pyplot as plt
#
# x = [0, 1, 2, 3, 4, 5]
# y = [0.1, 0.2, 0.2, 0.3, 0.2, 0.1]
#
# plt.plot(x, y,'--or')
#
# plt.show()

# import matplotlib.pyplot as plt
#
# month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# cost = [8, 7, 9, 9, 3, 10, 10, 12, 8, 6, 11, 10]
# profit = [12, 11, 11, 13, 5, 11, 13, 15, 10, 9, 12, 13]
#
# bar1 = plt.bar(month, profit, 0.5, color='y', linewidth=0, align='center')
# bar2 = plt.bar(month, cost, 0.5, color='g', linewidth=0, align='center')
#
# plt.legend( (bar1[0], bar2[0]), ('Profits', 'Costs') )
#
# plt.show()

# import matplotlib.pyplot as plt
#
# month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# cost = [8, 7, 9, 9, 3, 10, 10, 12, 8, 6, 11, 10]
# profit = [12, 11, 11, 13, 5, 11, 13, 15, 10, 9, 12, 13]
#
# bar1 = plt.barh(month, profit, 0.5, color='y', linewidth=0, align='center')
# bar2 = plt.barh(month, cost, 0.5, color='g', linewidth=0, align='center')
#
# plt.legend( (bar1[0], bar2[0]), ('Profits', 'Costs') )
#
# plt.show()

# import matplotlib.pyplot as plt
#
# rate = [1, 7, 3, 9]
#
# plt.pie(rate)
#
# plt.show()

# import matplotlib.pyplot as plt
#
# rate = [1, 7, 3, 9]
# explode = [0, 0, 0.1, 0]
# colors = ['c', 'm', 'y', 'g']
#
# plt.pie(rate, explode=explode, colors=colors)
#
# plt.show()

import matplotlib.pyplot as plt

rate = [1, 7, 3, 9]
explode = [0, 0, 0.1, 0]
colors = ['c', 'm', 'y', 'g']
labels = ['Apple', 'Pear', 'Peach', 'Orange']

plt.pie(rate, explode=explode, colors=colors, labels=labels, autopct='%d%%')

plt.show()