# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 13:29:43 2022

@author: Emmanuel Usman
"""
import math

def calculate(i, buns, fox):
    bpop_next = max(math.floor((10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop),0)
    fpop_next = max(math.floor(0.4 * fpop + 0.02 * fpop * bpop),0)
    i+=1
    return i, bpop_next, fpop_next

bpop = int(input('Number of bunnies ==> '))
print(bpop)
fpop = int(input('Number of foxes ==> '))
print(fpop)

i = 1

print('Year{0:.0f}: {1:.0f}, {2:.0f}'.format(i,bpop,fpop))
while i<5:
    x = calculate(i, bpop, fpop)
    i+=1
    print('Year{0:.0f}: {1:.0f}, {2:.0f}'.format(i,x[1],x[2]))
    bpop = x[1]
    fpop = x[2]