# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 23:10:01 2022

@author: Emmanuel Usman
"""

co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, 348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]

p = float(input("Enter the fraction: "))
print(p)

i = 0

for x in range(len(co2_levels)):
    co2_levels[x] = co2_levels[i]*(1+p)
    i+=1

print('First: {:.2f}'.format(co2_levels[0]))
print('Last: {:.2f}'.format(co2_levels[-1]))
