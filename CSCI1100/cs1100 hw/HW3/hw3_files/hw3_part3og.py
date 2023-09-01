# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 20:07:08 2022

@author: Emmanuel Usman
"""

turns = int(input("How many turns? => "))
print(turns)

name = input("What is the name of your pikachu? => ")
name = name.strip()
print(name)

enc = int(input("How often do we see a Pokemon (turns)? => "))
print(enc)
print('')
print("Starting simulation, turn 0 "+ name +" at (75, 75)")
record = []
loc = (75,75)
i=0
while i < turns:
    direc = input("What direction does {0:} walk? => ".format(name))
    direc = direc.strip()
    print(direc)
    i += 1
    if direc == "n" or direc == "N":
        loc = (loc[0] , loc[1]-5)
        if loc[0] > 150:
            loc = (150,loc[1])
        elif loc[0] < 0:
            loc = (0,loc[1])
        elif loc[1] > 150:
            loc = (loc[0],150)
        elif loc[1] < 0:
            loc = (loc[0],0)
    elif direc == "s" or direc == "S":
        loc = (loc[0] , loc[1]+5)
        if loc[0] > 150:
            loc = (150,loc[1])
        elif loc[0] < 0:
            loc = (0,loc[1])
        elif loc[1] > 150:
            loc = (loc[0],150)
        elif loc[1] < 0:
            loc = (loc[0],0)
    elif direc == "w" or direc == "W":
        loc = (loc[0] - 5 , loc[1])
        if loc[0] > 150:
            loc = (150,loc[1])
        elif loc[0] < 0:
            loc = (0,loc[1])
        elif loc[1] > 150:
            loc = (loc[0],150)
        elif loc[1] < 0:
            loc = (loc[0],0)
    elif direc == "e" or direc == "E":
        loc = (loc[0] + 5, loc[1])
        if loc[0] > 150:
            loc = (150,loc[1])
        elif loc[0] < 0:
            loc = (0,loc[1])
        elif loc[1] > 150:
            loc = (loc[0],150)
        elif loc[1] < 0:
            loc = (loc[0],0)
    if i % enc == 0:
        print("Turn {0:}, {1:} at ({2:}, {3:})".format(i, name, loc[1],loc[0]))
        p = input("What type of pokemon do you meet (W)ater, (G)round? => ")
        p = p.strip()
        print(p)
        if p == "g" or p == "G":
            if direc == "n" or direc == "N":
                loc = (loc[0], loc[1] + 10)
            elif direc == "s" or direc == "S":
                loc = (loc[0], loc[1] - 10 )
            elif direc == "e" or direc == "E":
                loc = (loc[0]-10, loc[1])
            elif direc == "w" or direc == "W":
                loc = (loc[0]+10, loc[1])
            print(name, 'runs away to (' + str(loc[1]) + ', ' + str(loc[0]) + ')')
            record.append("Lose")
        elif p == "w" or p == "W":
            if direc == "n" or direc == "N":
                loc = (loc[0], loc[1] - 1)
            elif direc == "s" or direc == "S":
                loc = (loc[0], loc[1] + 1 )
            elif direc == "e" or direc == "E":
                loc = (loc[0]+1, loc[1])
            elif direc == "w" or direc == "W":
                loc = (loc[0]-1, loc[1])
            print(name, 'wins and moves to (' + str(loc[1]) + ', ' + str(loc[0]) + ')')
            record.append("Win")
        else:
            record.append("No Pokemon")
print(name+" ends up at ("+ str(loc[1])+", "+str(loc[0])+"), Record:", record)

        