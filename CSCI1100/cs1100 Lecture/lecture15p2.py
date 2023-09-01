# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 17:33:13 2022

@author: Emmanuel Usman
"""

datafile = input("Data file name: ")
print(datafile)
datafile = datafile.strip()
prefix = input('Prefix: ')
print(prefix)
prefix = prefix.strip()

listoflines = []
f = open(datafile,'r')

i = 0
while i < len():
    line = f.readline()
    listoflines.append(line)
    i+=1
