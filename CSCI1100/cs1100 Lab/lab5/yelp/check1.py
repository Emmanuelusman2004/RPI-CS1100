# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 13:28:27 2022

@author: Emmanuel Usman
"""

import lab05_util

restaurants = lab05_util.read_yelp('yelp.txt')
print(restaurants[0])
print("")
def print_info(y):
    print(restaurants[y][0] + " (" + restaurants[y][5] + ")")
    x = restaurants[y][3].split("+")
    print("    " + x[0])
    print("    " + x[1])
    avgscore = sum(restaurants[y][-1])/len(restaurants[y][-1])
    print("Average Score: {0:.2f}".format(avgscore))
    print("")

#testing
print_info(0)
print_info(4)
print_info(42)
    