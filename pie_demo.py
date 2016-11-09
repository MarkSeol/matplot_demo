#!/usr/bin/python2.7
import matplotlib.pyplot as plt

slices = [7, 2, 4, 11]
activities = ['sleeping', 'eating', 'working', 'playing']
colors = ['c', 'm', 'r', 'b']

plt.pie(slices, labels=activities,
        colors=colors,
        startangle=90,              # startangle sets the first slice's angle
        shadow=True,
        explode=[0, 0.3, 0, 0],
        autopct='%1.1f%%')          # display size in % on each slice of pie

plt.title('Pie')
plt.legend()
plt.show()