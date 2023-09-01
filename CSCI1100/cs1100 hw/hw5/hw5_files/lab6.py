# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 13:07:40 2022

@author: Emmanuel Usman
"""


line = ""
for n in range(8):
    line = line + str(n) + " " 
print(line + "\n")

pairs = []
numbrs = [0,1,2,3,4,5,6,7,8]
for v in numbrs:
    i = 0
    while i <= 8:
        pair = v,i
        pairs.append(pair)
        i+=1
print(pairs)
print("")
i = 0


print("")
print("")

while i < len(pairs):
    if pairs[i][1] == 8 and (pairs[i] != (2,8) and pairs[i] != (5,8)):
        print(str(pairs[i][0]) + "," + str(pairs[i][1]))
    elif pairs[i] == (2,8) or pairs[i] == (5,8):
        print(str(pairs[i][0]) + "," + str(pairs[i][1])+ "\n")
    elif ((i+1) % 3) == 0 and i != 0:
        print(str(pairs[i][0]) + "," + str(pairs[i][1]) , end = "  ")
    else:
        print(str(pairs[i][0]) + "," + str(pairs[i][1]) , end = " ")
    i+=1
    
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














