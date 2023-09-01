# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 23:39:22 2022

@author: Emmanuel Usman
"""

turns = int(input("How many turns? => "))
print(turns)

name = input("What is the name of your pikachu? => ")
print(name)

enc = int(input("How often do we see a Pokemon (turns)? => "))
print(enc)

print("Starting simulation, turn 0", name , "at (75,75)")
#starting the loop for the simulation
x = 75
y = 75

def d_turns(x,y):
    i = 0
    while i < enc:
        d = input("What direction does {0} walk? => ".format(name))
        print(d)
        if d == "n" or d == "N":
            b = y - 5
            y = b
        elif d == "s" or d == "S":
            b = y + 5
            y = b
        elif d == "w" or d == "W":
            a = x - 5
            x = a
        elif d == "e" or d == "E":
            a = x + 5
            x = a
        print(x,y)
        i+=1
    return x,y,d

def encounters(x,y):
    





