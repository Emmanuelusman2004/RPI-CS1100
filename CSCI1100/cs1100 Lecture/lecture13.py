# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 22:07:28 2022

@author: Emmanuel Usman
"""

f = open("census_data.txt")
line1 = f.readline()
line1 = line1.strip()
line2 = f.read()
line3 = f.readline()
print(line1)
print(line2)
print(line3)
f.close()
f = open("census_data.txt")
s = f.read()
line_list = s.split('\n')
print(len(line_list))
line_list = s.strip().split('\n')
print(len(line_list))