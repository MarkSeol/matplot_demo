#!/usr/bin/python2.7
#coding:utf8

"""
File Name :		tutorial_29.py
Creation Date :		2016-10-27
Last Modified :
Created By :            markxue
Description :

"""

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()

ax1 = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
y = [5, 6, 7, 3, 4, 2, 7, 9, 3, 4]
z = [1, 1, 2, 3, 4, 5, 3, 3, 18, 8]

x2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
y2 = [-5, -6, -7, -8, -9, -2, -5, -6, -3, -7]
z2 = [1, 2, 6, 3, 2, 7, 3, 3, 7, 2]

ax1.scatter(x2, y2, z2, c='k', marker='o')
ax1.scatter(x, y, z, c='r', marker='*')

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

plt.show()
