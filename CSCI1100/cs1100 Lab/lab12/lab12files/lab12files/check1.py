# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 14:15:18 2022

@author: Emmanuel Usman
"""

def add(m,n):
    if n == 0:
        return m
    else:
        return add(m,n-1) + 1
print(add(5,3))

def mult(m,n):
    if n == 1:
        return m
    else:
        return add(mult(m,n-1) , m)

print(mult(8,3))

def power(m,n):
   if n == 1:
       return m
   else:
       return mult(power(m,n-1) , m)
    
print(power(6,3))