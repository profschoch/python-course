#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:56:07 2019

@author: peterschoch
"""
# perrin4.py
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




# ***********************
# Now we'll create a function for plotting.

def graphing_data(all_data,col_x,col_y):
# The next will be the docstring that explains what the function does and how.
    """
    The function accepts a NumPy array, a value to specify which column in
    the data it should use for the x-axis data, and a value to specify which
    column it should use for the y-axis data:
        graphing_data(NumPy array name,x column value,y column value)
    """        
    

    plt.figure(figsize=(10,10))
    plt.plot(all_data[:,col_x], all_data[:,col_y], 'r+', markersize=12)
    plt.axis([-20,20,-20,20])
    plt.grid(b=True,which='major',linestyle='-',linewidth=1.5,c='g')
    plt.show()
    answer=input("Do you want to save the plot?  (y/n)  ")
    if answer=='y' or answer=='Y':
        fig=plt.gcf()
        plt.savefig("plot_output.png")

#Notice you can't/shouldn't call a function before you define it!
x_val=input("Which column in the data file should I use to plot? ")
y_val=input("\nWhich column should I use in the data file for the y-axis? ")
graphing_data(data_set,int(x_val),int(y_val))