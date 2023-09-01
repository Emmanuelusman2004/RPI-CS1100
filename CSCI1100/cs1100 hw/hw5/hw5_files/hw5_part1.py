# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 13:55:10 2022

@author: Emmanuel Usman
"""

import hw5_util

def printgrid(gridnum):
    x = hw5_util.get_grid(gridnum)
    string = ""
    for n in range(len(x)):
        for s in range(len(x[0])):
            g = x[n][s]
            while len(str(g)) < 4:
                g = " " + str(g)
            string = string + g
        if n != len(x)-1:    
            string+=  "\n"
    print("Grid {0:}".format(gridnum))
    print(string)
    
def findneighbors(tup,maxrow,maxcol):
        neighbors = [(tup[0]-1, tup[1]), (tup[0], tup[1]-1), (tup[0], tup[1]+1), (tup[0]+1, tup[1])]
        trun = []
        for n in neighbors:
            if (n[0] >= 0 and  n[0] < maxrow) and (n[1] >= 0 and n[1] < maxcol):
                trun.append(n)
        return trun

i = 0
while i < 1:
    grid = int(input("Enter a grid index less than or equal to 3 (0 to end): "))
    print(grid)
    if grid == 1 or grid == 2 or grid ==3:
        pg = input("Should the grid be printed (Y or N): ")
        print(pg)
        pg = pg.strip()
        if pg == "y" or pg == "Y":
            printgrid(grid)
            x = hw5_util.get_grid(grid)
            print("Grid has {0:} rows and {1:} columns".format(len(x),len(x[1])))
            startloc = hw5_util.get_start_locations(grid)
            for sl in startloc:
                print("Neighbors of {0:}:".format(sl), end = "")
                ns = findneighbors(sl, len(x), len(x[1]))
                temp = ""
                for trun in ns:
                    temp = temp + " " + "("+str(trun[0])+", "+str(trun[1])+")"
                print(temp)
            path = hw5_util.get_path(grid)
            i = 1
            torf = True
            invalidpathtups = []
            totaldown = 0
            totalup = 0
            while i < len(path):
                deez = findneighbors((path[i-1]), len(x), len(x[1]))
                if x[path[i-1][0]][path[i-1][1]] - x[path[i][0]][path[i][1]] > 0:
                    totaldown=totaldown+(x[path[i-1][0]][path[i-1][1]] - x[path[i][0]][path[i][1]])
                else:
                    totalup-=(x[path[i-1][0]][path[i-1][1]] - x[path[i][0]][path[i][1]])
                if deez in path[i] == False:
                    torf = False
                    invalidpathtups.append(path[i])
                    invalidpathtups.append(path[i-1])
                i+=1
            if torf:
                print("Valid path")
                print("Downward {0:}".format(totaldown))
                print("Upward {0:}".format(totalup))
            else: 
                print("Path: invalid step from ({0:},{1:}) to ({2:},{3:})".format(invalidpathtups[0][0],invalidpathtups[0][1],invalidpathtups[1][0],invalidpathtups[1][1]))
        else:
            x = hw5_util.get_grid(grid)
            print("Grid has {0:} rows and {1:} columns".format(len(x),len(x[1])))
            startloc = hw5_util.get_start_locations(grid)
            for sl in startloc:
                print("Neighbors of {0:}:".format(sl), end = "")
                ns = findneighbors(sl, len(x), len(x[1]))
                temp = ""
                for trun in ns:
                    temp = temp + " " + "("+str(trun[0])+", "+str(trun[1])+")"
                print(temp)
            path = hw5_util.get_path(grid)
            i = 1
            torf = True
            invalidpathtups = []
            totaldown = 0
            totalup = 0
            while i < len(path):
                deez = findneighbors((path[i-1]), len(x), len(x[1]))
                if x[path[i-1][0]][path[i-1][1]] - x[path[i][0]][path[i][1]] > 0:
                    totaldown=totaldown+(x[path[i-1][0]][path[i-1][1]] - x[path[i][0]][path[i][1]])
                else:
                    totalup-=(x[path[i-1][0]][path[i-1][1]] - x[path[i][0]][path[i][1]])
                    
                if (path[i] not in deez):
                    torf = False
                    invalidpathtups.append(path[i])
                    invalidpathtups.append(path[i-1])
                    i = len(path)
                i+=1
            if torf == True:
                print("Valid path")
                print("Downward {0:}".format(totaldown))
                print("Upward {0:}".format(totalup))
            else: 
                print("Path: invalid step from ({0:}, {1:}) to ({2:}, {3:})".format(invalidpathtups[1][0],invalidpathtups[1][1],invalidpathtups[0][0],invalidpathtups[0][1]))
            
    else:
        i+=0    
    
    
    