#!/usr/bin/python2.7
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 7, 4]

x2 = [1, 2, 3]
y2 = [10, 15, 12]

plt.plot(x, y, label='First line')
plt.plot(x2, y2, label='Second line')

plt.xlabel('Plot Number')
plt.ylabel('Important value')

plt.title('Interesting Graph\nTest')
plt.legend()
plt.show()