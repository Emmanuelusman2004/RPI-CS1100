# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 18:16:14 2022

@author: Emmanuel Usman
"""

import hw5_util

def findneighbors(tup,maxrow,maxcol):
        neighbors = [(tup[0]-1, tup[1]), (tup[0], tup[1]-1), (tup[0], tup[1]+1), (tup[0]+1, tup[1])]
        trun = []
        for n in neighbors:
            if (n[0] >= 0 and  n[0] < maxrow) and (n[1] >= 0 and n[1] < maxcol):
                trun.append(n)
        return trun
    
def localmax(grid, courd):
    x = hw5_util.get_grid(grid)
    y = findneighbors(courd, len(x), len(x[1]))
    torf = True
    for item in y:
        if x[courd[0]][courd[1]] - x[item[0]][item[1]] < 0:
            torf = False
    return torf

def stepcheck(grid, courd, maxsteps):
    x = hw5_util.get_grid(grid)
    y = findneighbors(courd, len(x), len(x[1]))
    for item in y:
        if ((x[item[0]][item[1]]) - (x[courd[0]][courd[1]])) <= maxsteps and ((x[item[0]][item[1]]) - (x[courd[0]][courd[1]])) > 0:
            return True

def hon(grid,courd,maxsteps):
    x = hw5_util.get_grid(grid)
    y = findneighbors(courd, len(x), len(x[1]))
    neighd = []
    neighdc = []
    for item in y:
        if ((x[item[0]][item[1]]) - (x[courd[0]][courd[1]])) <= maxsteps and ((x[item[0]][item[1]]) - (x[courd[0]][courd[1]])) > 0:
            c = (x[item[0]][item[1]]) - (x[courd[0]][courd[1]])            
            neighd.append(c)
            neighdc.append(item)
    indx = neighd.index(max(neighd))
    honcourds = neighdc[indx]
    return honcourds
def lon(grid,courd,maxsteps):
    x = hw5_util.get_grid(grid)
    y = findneighbors(courd, len(x), len(x[1]))
    neighd = []
    neighdc = []
    for item in y:
        if ((x[item[0]][item[1]]) - (x[courd[0]][courd[1]])) <= maxsteps and ((x[item[0]][item[1]]) - (x[courd[0]][courd[1]])) > 0:
            c = (x[item[0]][item[1]]) - (x[courd[0]][courd[1]])            
            neighd.append(c)
            neighdc.append(item)
    indx = neighd.index(min(neighd))
    honcourds = neighdc[indx]
    return honcourds
            
def steepest(grid,startinglocation,maxsteps):
    path = [startinglocation]
    while startinglocation != truemaxnumcourds and localmax(grid,startinglocation) == False and stepcheck(grid,startinglocation,maxsteps) == True:  
        startinglocation = hon(grid, startinglocation, maxsteps)
        path.append(startinglocation)
    return path
            
def gradual(grid,startinglocation,maxsteps):
    path = [startinglocation]
    while startinglocation != truemaxnumcourds and localmax(grid,startinglocation) == False and stepcheck(grid,startinglocation,maxsteps) == True:  
        startinglocation = lon(grid, startinglocation, maxsteps)
        path.append(startinglocation)
    return path

def typemax(grid, courd, globalmax):
    if courd == globalmax:
        print("global maximum")
    elif localmax(grid, courd):
        print("local maximum")
    else:
        print('no maximum')

def printpath(path):
    string = ""
    i = 0
    while i < len(path):
        if (i+1)%5==0 and i != 0 and len(path) != 5:
            string+= "{} \n".format(path[i])
        else:
            string+= "{} ".format(path[i])
        i+=1
    print(string)
def printgrid(grid):
    string = ""
    for n in range(len(grid)):
        for s in range(len(grid[0])):
            g = grid[n][s]
            if g == 0:
                g = "."
            while len(str(g)) < 3:
                g = " " + str(g)
            string = string + str(g)
        if n != len(grid)-1:    
            string+=  "\n"
    print(string)

grid = int(input("Enter a grid index less than or equal to 3 (0 to end): "))
print(grid)
maxsteph = int(input("Enter the maximum step height: "))
print(maxsteph)
printpaths = input("Should the path grid be printed (Y or N): ")
print(printpaths)
x = hw5_util.get_grid(grid)
print("Grid has {0:} rows and {1:} columns".format(len(x),len(x[1])))
maxnums = []
maxnumcourds = []
i = 0
for j in x:
    maxnums.append(max(j))
    for num in j:
        if num == max(j):
            z = j.index(num)
            maxnumcourds.append((i,z))
    i+=1
truemaxnumcourds = maxnumcourds[maxnums.index(max(maxnums))]
print("global max: {0:} {1:}".format(truemaxnumcourds,max(maxnums)))
startlocations = hw5_util.get_start_locations(grid)
print("===")
pathsss = []
for mynutsackinyourface in startlocations:
    print("steepest path")
    steepath = steepest(grid,mynutsackinyourface,maxsteph)
    pathsss.append(steepath)
    printpath(steepath)
,m,mm    print("...")
    print("most gradual path")
    mgp = gradual(grid,mynutsackinyourface,maxsteph)
    pathsss.append(mgp)
    printpath(mgp)
    typemax(grid,mgp[-1],truemaxnumcourds)
    print("===")
if printpaths == "y" or printpaths == "Y":
    print("Path grid")
    newgridog = []
    for n in x:
        newrow = []
        for s in n:
            newrow.append(0)
        newgridog.append(newrow)
    for n in pathsss:
        for a in n:
            newgridog[a[0]][a[1]]+=1
    printgrid(newgridog)
    
        
        
    