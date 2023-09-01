# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:51:46 2022

@author: Emmanuel Usman
"""

def convert2fahren(celsius):
    fahrenheight = (1.8 * celsius) + 32
    return fahrenheight
convert2fahren(0)
convert2fahren(32)
convert2fahren(100)

print("0 -> ", convert2fahren(0))
print("32 -> ", convert2fahren(32))
print("100 ->", convert2fahren(100))
