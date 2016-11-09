#!/usr/bin/python2.7
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]

sleeping = [7, 8, 7, 9, 7, 8, 8]
eating = [2, 2, 3, 2, 1, 2, 3]
working = [12, 13, 12, 12, 13, 1, 1]
playing = [3, 1, 2, 1, 3, 13, 12]

# plot empty data, just for print the legends, linewidth if set for the legends
plt.plot([], [], label='Sleeping', color='m', linewidth=5)
plt.plot([], [], label='Eating', color='c', linewidth=5)
plt.plot([], [], label='Working', color='r', linewidth=5)
plt.plot([], [], label='Playing', color='k', linewidth=5)

plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'])

plt.xlabel('Day of week')
plt.ylabel('Hours')

plt.title('stack plot')
plt.legend()
plt.show()