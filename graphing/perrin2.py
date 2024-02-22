#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:56:07 2019

@author: peterschoch
"""
# perrin2.py
# -------------------------------------------------------------------------
# This program accepts Perrin's data for Brownian motion as a simple file
# input example.  I will do some math on it, display it, and use it later to 
# demonstrate plotting using pyplot.
# ------------------------------------------------------------------------- 
import numpy as np
import matplotlib.pyplot as plt

data_set = np.loadtxt("g26perrindata.csv", delimiter=',')
# See how easy that is using NumPy.  Since most of us are more familiar with
# math ideas, it is better to do it this way 
# (unless you're going to use Pandas).


# If you are using Spyder, you should use the Variable Explorer to see what 
# data_set "looks like".  I'm going to use functions from NumPy to output
# some salient information

print('The size of the data set array is:  ',np.size(data_set))
print('The shape of the data set array is:  ',np.shape(data_set))
# What do those 2 sets of output mean?!  Before proceeding, you should 
# know that.

print(data_set)
# Notice that it won't print out the whole array, it gives the first 3 and
# last 3 rows in the array with an ellipsis in the middle.

# Now, I want to slice off sections of the array to create "vectors" that
# could be used to plot the data.
N=np.size(data_set,0)
print('The number of rows in the data set array is:  ',N)

x_values=data_set[0:N:1, 0]
# we start at the 1st value in the first column, do this for N rows, 1 step at 
# a time.
y_values=data_set[0:N:1,1]

print('The size of the x set array is:  ',np.size(x_values))
print('The shape of the x set array is:  ',np.shape(x_values))
print(x_values)
print('The max value of the x data is:  ',np.max(x_values))
print('The minimum value of the x data is:  ',np.min(x_values))
print('The mean of the x data is:  ',np.mean(x_values))
print('The standard deviation of the x data is:  ',np.std(x_values))

print('The size of the y set array is:  ',np.size(y_values))
print('The shape of the y set array is:  ',np.shape(y_values))
print(y_values)
print('The max value of the y data is:  ',np.max(y_values))
print('The minimum value of the y data is:  ',np.min(y_values))
print('The mean of the y data is:  ',np.mean(y_values))
print('The standard deviation of the y data is:  ',np.std(y_values))

plt.figure(figsize=(10,10))
plt.plot(x_values, y_values, 'b.', markersize=12)
