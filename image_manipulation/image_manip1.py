#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue OCT 15 19:56:07 2020

@author: peterschoch
"""
# image_manip.py
# -------------------------------------------------------------------------
# This program is designed to import an image, and then
#  then perform some manipulations and calculations 
#  on the image and its array and output the altered
#  image.
# ------------------------------------------------------------------------- 
#import numpy as np
#import matplotlib.pyplot as plt
#  This next line imports the Python Image Library
from PIL import Image, ImageFilter


def roll(image, delta):
    """Roll an image sideways."""
    xsize, ysize = image.size

    delta = delta % xsize
    if delta == 0: return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    image.paste(part1, (xsize-delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize-delta, ysize))

    return image
#So, I freely admit I stole this function!  



photo=Image.open('3.jpg')
# This imports the photo using the built-in function.

#  Rather than using the plt functions to output the image immediately, 
#    I want to use the Image functions to do so.

photo.show()
#  Notice, it will open a new window to display it!

#  Now, let's see some information about the image.
print(photo.format, photo.size, photo.mode)

#How about applying some filters to change the image?
f1 = photo.filter(ImageFilter.BLUR)
f1.show()

f2 = photo.filter(ImageFilter.EDGE_ENHANCE)
f2.show()

f3 = photo.filter(ImageFilter.CONTOUR)
f3.show()

f4 = photo.filter(ImageFilter.SMOOTH)
f4.show()

# Does it look like I'm making a photo editor?  Do any of these look 
#  familiar to any of you?!

#  You can rotate the image by any degree, as well.
photo.rotate(30).show()

#  Need to create thumbnail of an image?
photo.thumbnail((150,150))

photo.show()

photo2=photo

#  How about cropping an image?
#  (0,0) is the upper left.  
#  The coordinates are (left, upper, right, lower).
box = (0,0,981,480)
region = photo2.crop(box)

region.show()


roll(photo2,5000).show()
#Try changing the value in the 5000 spot to different things and look carefully
#  at the results!  I think this is very cool.



