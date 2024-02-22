#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:56:07 2019

@author: peterschoch
"""
# gen_plot.py
# -------------------------------------------------------------------------
# This program is built upon the perrin4.py program.
#  It has 3 main parts to it:
#  1.  I create a GUI to ask the user for the data to be imported (filename).
#  2.  I ask for what data is to extracted from the file.
#  3.  I ask what columns to graph.
# ------------------------------------------------------------------------- 
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

def get_file():
    """
    The function is designed to open a simple GUI window to allow the user
    to choose the data file to be used.  The function returns the file name 
    along with its path.
    """
    print("Use the GUI window to choose the csv data file to process." )
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    return filename


def graphing_data(all_data,lines,col_x,col_y):
# The next will be the docstring that explains what the function does and how.
    """
    The function accepts a NumPy array,
    a values for how many lines should be on the graph, 
    a value to specify which column contains the x data,
    and a value to specify which column(s) it should use for the y-axis data:
        graphing_data(NumPy array name,number of lines,x column value,y column value)
    """        
    

    plt.figure(figsize=(10,10))
    for n in range(0,lines):
        temp=col_y[0,n]
        name="Data from column "+str(temp)
        plt.plot(all_data[:,col_x], all_data[:,temp],label=name  )
    plt.grid(b=True,which='major',linestyle='-',linewidth=1.0,c='g')
    plt.legend()
    plt.show()

name=get_file()

data_set = np.loadtxt(name, delimiter=',')
# See how easy that is using NumPy.  Since most of us are more familiar with
# math ideas, it is better to do it this way 
# (unless you're going to use Pandas).




# ***********************
y_val=np.empty([1,4], dtype=int)

#Notice you can't/shouldn't call a function before you define it!
lines=input("how many columns in the data set do you want to plot against the common x-axis? ")
x_val=input("Which column in the data file is the independent axis? ")
for n in range(0,int(lines)):
        temp=input("\nWhich column should I use in the data file for the y-axis? ")
        y_val[0,n]=int(temp)
        print(y_val[0,n])
graphing_data(data_set,int(lines),int(x_val),y_val)