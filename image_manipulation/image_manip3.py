#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue OCT 15 19:56:07 2020

@author: peterschoch
"""
# image_manip3.py
# -------------------------------------------------------------------------
# This program is designed to import an image as an array, and then
#  then perform some calculations on the array and output the altered
#  image.
# ------------------------------------------------------------------------- 
import numpy as np
import matplotlib.pyplot as plt

import scipy.ndimage as sim

import imageio

def vertical_gradient(image, reverse=False):
    """
        Creates a horizontal line with the shape (1, image.shape, 3)
        The values are incremented from 0 to 1, if reverse is False;
        otherwise the values are decremented from 1 to 0.
        
        Function shamelessly stolen from an online source.
    

    Parameters
    ----------
    image : np array
    reverse : logical, optional
        

    Returns value
    -------
   

    """
    number_of_columns = image.shape[1]
    if reverse:
        C = np.linspace(1,0,number_of_columns)
    else:
        C = np.linspace(0,1,number_of_columns)
    C=np.dstack((C,C,C))
    return C

def horizontal_gradient(image):
    """
        Creates a vertical line with the shape (image.shape, 1, 3)
        
        
        Function shamelessly stolen from an online source.
    

    Parameters
    ----------
    image : np array
    reverse : logical, optional
        

    Returns value
    -------
   

    """
    number_of_rows, number_of_columns = image.shape[:2]
    C=np.linspace(1,0,number_of_rows)
    C=C[np.newaxis,:]
    C=np.concatenate((C,C,C)).transpose()
    C=C[:,np.newaxis]
    return C




photo = imageio.imread('3.jpg').astype(float)

#  Use of a Gaussian filter
blur = sim.gaussian_filter(photo,sigma=5)

plt.figure()
plt.imshow(blur/blur.max())
plt.axis('off')



f_blur = sim.gaussian_filter(blur,1)

plt.figure()
plt.imshow(f_blur/f_blur.max())

# A way to sharpen an image.
sharp = blur + 30.0*(blur-f_blur)
sharp=sharp/sharp.max()
sharp[sharp<0]=0
plt.figure()
plt.imshow(sharp)

# A way to introduce noise into an image.
noise = photo+0.6*photo.std()*np.random.random(photo.shape)

plt.figure()
plt.imshow(noise/noise.max())
plt.axis('off')

#  How to remove noise from an image.
denoised=sim.median_filter(noise,5)

plt.figure()
plt.imshow(denoised/denoised.max())

tinted = photo+(np.ones(photo.shape)-photo)*0.75
#"Play" with the number 0.75 between 0 and 1 to see what happens here!
plt.figure()
plt.imshow(tinted/tinted.max())



horizontal_brush = vertical_gradient(photo)
tinted = photo*horizontal_brush
plt.figure()
plt.axis('off')
plt.imshow(tinted/tinted.max())


vertical_brush = horizontal_gradient(photo)
tinted = photo*vertical_brush
plt.figure()
plt.axis('off')
plt.imshow(tinted/tinted.max())
