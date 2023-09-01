# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 14:49:10 2022

@author: Emmanuel Usman
"""
def make_square(image):
    x , y  = image.size    
    if x > y:
        im = image.crop((0,0,y,y))
    else:
        im = image.crop((0,0,x,x))
    return im

