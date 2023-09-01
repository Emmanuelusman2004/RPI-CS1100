# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 16:26:38 2022

@author: Emmanuel Usman
"""
import lab06_util
def ok_to_add(r,c,num,bd):
    safe = True
    r = int(r)
    c = int(c)
    num = int(num)
    if r<0 or r>9 or c<0 or c>9 or num<0 or num>9:
        safe = False
    for x in range(0,9):
        if bd[r][c] ==str(x):
            safe = False
    for col in bd[r]:
        if col == str(num):
            safe = False
    for row in bd:
        if row[c]==str(num):
            safe = False
    rBox = r%3
    cBox = c%3
    for x in range(rBox*3, rBox*3+2):
        for y in range(cBox*3, cBox*3+2):
            if bd[x][y]==num:
                safe == False
    if safe == True:
        bd[r][c] = str(num)
    elif safe == False:
        print("This number cannot be added")
    return bd

bdfile = input("Enter sudokufile: ")
bd = lab06_util.read_sudoku(bdfile)
sudokucomplete = False
periodcount = 0
rowwindex = 0
for roww in bd:
    collindex = 0
    for coll in roww:
        if coll == ".":
            periodcount+=1
        elif (rowwindex ==8 and collindex ==5 and periodcount ==0):
            sudokucomplete = True
        collindex+=1
    rowwindex+=1
rindex=0
print("-----------------------------")
for r in bd:
    print("| ", end = "")
    cindex = 0
    for c in r:
        print(str(c)+" ", end = "")
        if cindex!=0 and (cindex==2 or cindex ==5 or cindex ==8):
            print("| ", end = "")
        cindex+=1
    print()
    if (rindex !=0) and (rindex==2 or rindex ==5 or rindex==8):
        print("-------------------------")
    rindex+=1
print()
while (sudokucomplete == False):
    rowinput=(input("Enter row: "))
    colinput=(input("Enter col: "))
    numinput=(input("Enter num: "))
    bd=ok_to_add(rowinput,colinput,numinput,bd)
    rindex=0
    print("-------------------------")
    for r in bd:
        print("| ", end = "")
        cindex = 0
        for c in r:
            print(str(c)+" ", end = "")
            if cindex!=0 and (cindex==2 or cindex ==5 or cindex ==8):
                print("| ", end = "")
            cindex+=1
        print()
        if (rindex !=0) and (rindex==2 or rindex ==5 or rindex==8):
            print("-------------------------")
        rindex+=1
    print()
    periodcount = 0
    rowwindex=0
    for roww in bd:
        collindex = 0
        for coll in roww:
            if coll == ".":
                periodcount+=1
            elif (rowwindex ==8 and collindex ==5 and periodcount ==0):
                sudokucomplete = True
            collindex+=1
        rowwindex+=1
        