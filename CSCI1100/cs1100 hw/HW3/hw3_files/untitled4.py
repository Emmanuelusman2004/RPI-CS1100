# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 20:51:39 2022

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
    while i < turns/(turns/enc):
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
def encounters(x,y): #takes the first courds
    i = 0
    while i <= ((turns-enc)/enc):
        list_cd = d_turns(x,y) #loops the directions to find the courdinates and direction
        if i < ((turns-enc)/enc): 
            wg = input("What type of pokemon do you meet, (W)ater, (G)round? => ")
            if wg == "w" or wg == "W":
                if list_cd[2] == "n" or list_cd[2] == "N":
                    b = list_cd[1] - 1
                    print(b)
                    y = b
                elif list_cd[2] == "s" or list_cd[2] == "S":
                    b = list_cd[1] + 1
                    y = b
                elif list_cd[2] == "w" or list_cd[2] == "W":
                    a = list_cd[1] - 1
                    x = a
                elif list_cd[2] == "e" or list_cd[2] == "E":
                    a = list_cd[1] + 1
                    x = a
            elif wg == "g" or wg == "G":
                 if list_cd[2] == "n" or list_cd[2] == "N":
                     b = list_cd[1] + 10
                     y = b
                 elif list_cd[2] == "s" or list_cd[2] == "S":
                     b = list_cd[1] - 10
                     y = b
                 elif list_cd[2] == "w" or list_cd[2] == "W":
                     a = list_cd[1] + 10
                     x = a
                 elif list_cd[2] == "e" or list_cd[2] == "E":
                     a = list_cd[1] - 10
                     x = a
        i+=1
#print("Turn 2 {0} at {1}".format(name,d_turns(x,y)))

