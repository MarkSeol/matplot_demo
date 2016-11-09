#!/usr/bin/python2.7

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 3, 4, 5, 6]

plt.scatter(x, y, label='skitscat', color='c', marker='*', s=100)
# marker, change dot to star,  s size of the marker

plt.xlabel('x')
plt.ylabel('y')

plt.title('Interesting Graph\nTest')
plt.legend()
plt.show()