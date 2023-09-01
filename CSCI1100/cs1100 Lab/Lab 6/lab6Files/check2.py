# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 13:34:38 2022

@author: Emmanuel Usman
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 13:07:40 2022

@author: Emmanuel Usman
"""    
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

print("")

bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

string = ""
for n in range(len(bd)):
    if n%3 == 0:
        string+= "-"*25+"\n"
    for x in range(len(bd[0])):
        if x%3==0:
            string+="| "
        string = string + bd[n][x] + " "
    string+=  "|\n"
string+= "-"*25
print(string)

sudokucomplete = False
while (sudokucomplete == False):
    periodcount = 0
    for rr in bd:
        for cc in rr:
            if cc == ".":
                periodcount = periodcount+1
            elif (rr==8 and cc==8 and periodcount ==0):
                sudokucomplete= True
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
        print("")
        if (rindex !=0) and (rindex==2 or rindex ==5 or rindex==8):
            print("-------------------------")
        rindex+=1
    print()
    rowinput=(input("Enter row: "))
    colinput=(input("Enter col: "))
    numinput=(input("Enter num: "))
    bd=ok_to_add(rowinput,colinput,numinput,bd)
        
    



