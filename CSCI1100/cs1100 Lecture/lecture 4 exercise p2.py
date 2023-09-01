# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 10:14:44 2022

@author: Emmanuel Usman
"""

import math

radius = 5
radius2 = 32

pi = math.pi

area1 = pi*(radius ** 2)
area2 = pi*(pow(radius2,2))

print("Area 1 = ", round(area1,2))

txt1 = "Area 2 = {areas}".format(areas = round(area2,2))
print(txt1)