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




# ***********************
# There is another way to access the data to be plotted!

plt.figure(figsize=(10,10))
plt.plot(data_set[:,0], data_set[:,1], 'r+', markersize=12)
plt.axis([-20,20,-20,20])
plt.grid(b=True,which='major',linestyle='-',linewidth=1.5,c='g')
plt.xlabel('$\\Delta x$ [$\\mu$m]', fontsize=20)
plt.ylabel('$\\Delta y$ [$\\mu$m]', fontsize=20)

#  What if we want to save the graph?!
fig=plt.gcf()
#This Gets the Current Figure, if you plot more than one it is the latest.
plt.savefig("plot_output.png")
#  This should save where the program is located.  
#  To see more file types to save as:  fig.canvas.get_supported_filestypes()