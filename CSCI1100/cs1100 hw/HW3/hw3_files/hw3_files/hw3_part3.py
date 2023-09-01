# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 13:23:05 2022

@author: Emmanuel Usman
"""
import math


def tourists(bears):
    if bears<4 or bears>15:
        tourists = 0
    elif bears > 10:
        tourists = (10000*10) + (20000*(bears-10))
    elif bears <10:
        tourists = 10000 * bears
    return tourists
def bearsnberries(bears,berries,tourists):
    bears_next = max(berries/(50*(bears+1)) + bears*0.60 - (math.log(1+tourists,10)*0.1),0)
    berries_next = max((berries*1.5) - (bears+1)*(berries/14) - (math.log(1+tourists,10)*0.05),0)
    return math.floor(bears_next),berries_next,tourists
def yearstats(bears,berries):
    t = tourists(bears)
    bnb = bearsnberries(bears, berries, t)
    print("Years     Bears    Berry        Tourists")
    print("1         5        200.0        {0:.0f}".format(bnb[2]))
    print("2         {0:.0f}        {1:.1f}        {2:.0f}".format(bnb[0],bnb[1],bnb[2]))
    b = []
    be = []
    to = []
    i = 0
    while i < 8:
        t = tourists(bnb[0])
        bnb = bearsnberries(bnb[0], bnb[1], t)
        b.append(bnb[0])
        be.append(bnb[1])
        to.append(bnb[2])
        if i+3 == 10:
            print("{0:.0f}        {1:.0f}        {2:.1f}        {3:.0f}".format(i+3,bnb[0],bnb[1],bnb[2]))
        else: 
            print("{0:.0f}         {1:.0f}        {2:.1f}        {3:.0f}".format(i+3,bnb[0],bnb[1],bnb[2]))
        i+=1
    b.append(5)
    b.append(3)
    be.append(200)
    be.append(214.1)
    to.append(50000)
    to.append(0)
    b.sort()
    be.sort()
    to.sort()
    print("")
    print("Min:      {0:.0f}        {1:.1f}        {2:.0f}".format(b[0],be[0],to[0]))
    print("Max:      {0:.0f}        {1:.1f}        {2:.0f}".format(b[-1],be[-1],to[-1]))
bears = int(input("Number of bears => "))
print(bears)
berries = int(input("Size of berry area => "))
print(berries)

x = bears
y = berries

yearstats(x,y)
