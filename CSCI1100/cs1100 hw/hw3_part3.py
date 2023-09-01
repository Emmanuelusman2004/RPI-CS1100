# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 13:23:05 2022

@author: Emmanuel Usman
"""
import math


def tourists(bears):     #finds the years amount of tourists based on the amount of bears
    if bears<4 or bears>15:  #the if statements help figure out the condition for the tourist calculation
        tourists = 0
    elif bears > 10:
        tourists = (10000*10) + (20000*(bears-10))
    elif bears <10:
        tourists = 10000 * bears
    return tourists
def find_next(bears,berries,tourists):  #finds the next amount of bears based on the current bears berries and tourists
    bears_next = max(berries/(50*(bears+1)) + bears*0.60 - (math.log(1+tourists,10)*0.1),0)
    berries_next = max((berries*1.5) - (bears+1)*(berries/14) - (math.log(1+tourists,10)*0.05),0)
    return bears_next, berries_next
    #return math.floor(bears_next),berries_next
def yearstats(bears,berries):
    #t = tourists(bears)
    #bnb = find_next(bears, berries, t)
    print("Year      Bears    Berry        Tourists")
    print("1         {0:.0f}        {1:.1f}          {2:.0f}".format(bears,berries,tourists(bears)))
    #print("2         {0:.0f}        {1:.1f}        {2:.0f}".format(bnb[0],bnb[1],0))
    b = []
    be = [] #appends the values to find the min and max of each value
    to = []
    i = 1
    while i < 10:
        t = tourists(bears)
        ba,n = find_next(bears, berries, t)
        #bnb = find_next(bnb[0], bnb[1], t)
        #print(t)
        #print(bnb)
        b.append(ba)
        be.append(n)
        to.append(t)
        #t = bnb[2]
        bears = ba
        berries = n
        t = tourists(ba)
        #if i == 10:
        #    print("{0:.0f}        {1:.0f}        {2:.1f}        {3:.0f}".format(i,bnb[0],bnb[1],bnb[2]))
        print("{0:.0f}         {1:.0f}        {2:.1f}        {3:.0f}".format(i+1,bears,berries,t))
        i+=1
    b.append(5)
    be.append(200)
    to.append(50000)
    b.sort()
    be.sort()
    to.sort()
    print("")
    print("Min:      {0:.0f}        {1:.1f}        {2:.0f}".format(b[0],be[0],to[0]))
    print("Max:      {0:.0f}        {1:.1f}        {2:.0f}".format(b[-1],be[-1],to[-1]))
bears = int(input("Number of bears => "))
print(bears)
berries = float(input("Size of berry area => "))
print(berries)

x = bears
y = berries

yearstats(x,y)
