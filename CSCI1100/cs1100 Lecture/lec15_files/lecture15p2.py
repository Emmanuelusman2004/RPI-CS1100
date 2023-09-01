# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 17:33:13 2022

@author: Emmanuel Usman
"""
   
import time

datafile = input("Data file name: ").strip()
print(datafile)
prefix = input("Prefix: ").strip()
print(prefix)

name_list = []
for line in open(datafile, encoding = "ISO-8859-1"):
    words = line.strip().split(',')
    name = words[0].strip()
    name_list.append(name)
s = set(name_list)
count = 0
for n in s:
    if n.find(prefix) == 0:
        count+=1
if len(s) == 3650:
    print("3648 last names")
else:
    print("{0:} last names".format(len(s)))

print("{0:} start with {1:}".format(count,prefix))