# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:53:22 2022

@author: Emmanuel Usman
"""

hd = int(input("Enter Dale's height: "))
he = int(input("Enter Erin's height: "))
hs = int(input("Enter Sam's height: "))

if hd<he and he<hs:
    x = "Dale"
    y = "Erin"
    z = "Sam"
    l = (z,y,x)
    print("{0}\n{1}\n{2}".format(l[0],l[1],l[2]))
elif hd<hs and hs<he:
    x = "Dale"
    y = "Sam"
    z = "Erin"
    l = (z,y,x)
    print("{0}\n{1}\n{2}".format(l[0],l[1],l[2]))
elif he<hd and hd<hs:
    x = "Erin"
    y = "Dale"
    z = "Sam"
    l = (z,y,x)
    print("{0}\n{1}\n{2}".format(l[0],l[1],l[2]))
elif he<hs and hs<hd:
    x = "Erin"
    y = "Sam"
    z = "Dale"
    l = (z,y,x)
    print("{0}\n{1}\n{2}".format(l[0],l[1],l[2]))
elif hs<hd and hd<he:
    x = "Sam"
    y = "Dale"
    z = "Erin"
    l = (z,y,x)
    print("{0}\n{1}\n{2}".format(l[0],l[1],l[2]))
elif hs<he and he<hd:
    x = "Sam"
    y = "Erin"
    z = "Dale"
    l = (z,y,x)
    print("{0}\n{1}\n{2}".format(l[0],l[1],l[2]))
