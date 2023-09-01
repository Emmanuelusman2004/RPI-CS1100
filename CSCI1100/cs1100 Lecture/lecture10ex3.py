# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:08:58 2022

@author: Emmanuel Usman
"""

co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, 348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]

avg = sum(co2_levels) / len(co2_levels)

l = []

for i in co2_levels:
    if i > avg:
        l.append(i)

print("Average:", str(format(avg, ".2f")))
print("Num above average:", len(l))
