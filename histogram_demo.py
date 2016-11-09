#/usr/bin/python2.7
import matplotlib.pyplot as plt

population_ages = [11, 22, 34, 55, 14, 15, 45, 67, 23, 45, 111, 67, 56, 78, 58, 46, 37, 96, 65, 45, 34, 37]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

plt.hist(population_ages, bins, label='bars1', color='c')

plt.xlabel('x')
plt.ylabel('y')

plt.title('Histogram Graph')
plt.legend()
plt.show()