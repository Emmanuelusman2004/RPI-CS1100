# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 22:14:46 2022

@author: Emmanuel Usman
"""

x = input("Enter the scores file: ")
print(x)
y = input("Enter the output file: ")
print(y)
f = open(y,"w")
g = open(x)
listofscores = []
i = 0
for n in g:
    listofscores.append(int(n))
listofscores.sort()
for s in open(x):
    f.write("{0:2d}: {1:3d}\n".format(i,(listofscores[i])))
    i += 1    
f.close()