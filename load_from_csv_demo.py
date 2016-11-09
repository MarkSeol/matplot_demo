#!/usr/bin/python2.7
#import csv
import matplotlib.pyplot as plt
import numpy as np

x = []
y = []
#1. use numpy to load the data
x, y = np.loadtxt('data/test.csv', delimiter=',', unpack=True)  # unpack If True, two array x, y is returned

#2. use csv to load the data
#with open('data/test.csv', 'r') as csvfile:
#    plots = csv.reader(csvfile, delimiter=',')
#    for row in plots:
#        x.append(int(row[0]))
#        y.append(int(row[1]))

plt.plot(x, y, label='Loaded from file')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Load data from csv')
plt.legend()
plt.show()