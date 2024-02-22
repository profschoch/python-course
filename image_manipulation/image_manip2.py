#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue OCT 15 19:56:07 2020

@author: peterschoch
"""
# image_manip2.py
# -------------------------------------------------------------------------
# This program is designed to import an image as an array, and then
#  then perform some calculations on the array and output the altered
#  image.
# ------------------------------------------------------------------------- 
import numpy as np
import matplotlib.pyplot as plt

import scipy.ndimage as sim

import imageio

#First, I need to load the file as an array.
photo = imageio.imread('3.jpg')
#Check the Variable explorer for size, etc.



#Now, I'd like to output the array as an image.
plt.imshow(photo,cmap=plt.cm.gray)

plt.figure()
#  This makes sure that the original figure stays on the screen and then the 
#  output of the convolved one will appear below it.

#  I'd like to remove the "graph look"
plt.imshow(photo,cmap=plt.cm.gray, vmin=30, vmax=200)
plt.axis('off')


plt.figure()
#  This makes sure that the original figure stays on the screen and then the 
#  output of the convolved one will appear below it.

print('The average value in the image is',photo.mean())
print('The max and min values are:  ',photo.max(), photo.min())

#  For smooth intensity variations, use 'bilinear'
plt.imshow(photo[500:550,500:550],cmap=plt.cm.gray, interpolation='bilinear')

plt.figure()
#  This makes sure that the original figure stays on the screen and then the 
#  output of the convolved one will appear below it.

#  To inspect intensity vairations, use 'nearest'
plt.imshow(photo[500:550,500:550],cmap=plt.cm.gray, interpolation='nearest')

#Now for a bit of foolishness...


lx,ly,d=photo.shape
X,Y=np.ogrid[0:lx,0:ly]
mask=(X-lx/2)**2+(Y-ly/2)**2>lx*ly/4
photo[mask]=0
plt.figure()
plt.imshow(photo)

#cropping an image
lx,ly,d = photo.shape
crop_photo = photo[lx//4:-lx//4,ly//4:-ly//4]
plt.figure()
plt.imshow(crop_photo)

#try to guess what this does BEFORE you run the program!
f = np.flipud(photo)
plt.figure()
plt.imshow(f)


