#/usr/bin/python2.7
import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10]
y = [5, 6, 4, 2, 7]

x2 = [1, 3, 5, 7, 9]
y2 = [2, 3, 5, 5, 1]

plt.bar(x, y, label='bars1', color='r')
plt.bar(x2, y2, label='bars2', color='c')

plt.xlabel('x')
plt.ylabel('y')

plt.title('Interesting Graph\nTest')
plt.legend()
plt.show()