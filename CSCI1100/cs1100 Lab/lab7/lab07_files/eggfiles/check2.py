# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 15:23:54 2022

@author: Emmanuel Usman
"""

def parse_line(string):
    if (string.count("/") >= 3):
        text1 = string[::-1].partition("/")
        text2 = text1[2].partition("/")
        text3 = text2[2].partition("/")

        if (text1[0].isdigit() == True and text2[0].isdigit() == True and text3[0].isdigit() == True):
            tup = (int(text3[0][::-1]), int(text2[0][::-1]), int(text1[0][::-1]), text3[2][::-1])
            return tup
        else:
            return None
    else:
        return None

        
def get_line(fname,parno,lineno):
    text = open(fname)
    line = text.read()
    lines = line.splitlines()
    spaces = []
    for i in range(0,len(lines)):
        if (lines[i] == ""):
            spaces.append(i)
    double_space = []
    for i in range(1, len(spaces)):
        if (spaces[i] == spaces[i - 1] + 1):
            double_space.append(i-1)
    for i in range(0, len(double_space)):
        spaces.pop(double_space[i] - i)
    if (parno > 1):
        return lines[spaces[parno - 2] + lineno]
    else:
        return lines[lineno]

    
    
file = input("Please enter the file number: ")
file = file.strip()
para = input("Please enter the paragraph number: ")
para = para.strip()
line = input("Please enter the line number: ")
line = line.strip()
file = int(file)
para  = int(para)
line = int(line)
    
