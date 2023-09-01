# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 14:34:01 2022

@author: Emmanuel Usman
"""
census = [ 340, 589, 959, 1372, 1918, 2428, 3097, 3880, 4382, 5082, \
            5997, 7268, 9113, 10385, 12588, 13479, 14830, 16782, \
            8236, 17558, 17990, 18976, 19378 ]
avg_list =[]
i = 0
while i < len(census)-1:
    diff = census[i+1] - census[i]
    perc_change = (diff / census[i]) * 100
    avg_list.append(perc_change)
    i = i+1

sumavg = sum(avg_list)
avgdenom = (len(avg_list))

avg = round(sumavg/avgdenom,1)

print("Average = " + str(avg) + "%")