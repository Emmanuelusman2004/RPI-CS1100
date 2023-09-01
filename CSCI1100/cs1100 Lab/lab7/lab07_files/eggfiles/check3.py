# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:08:45 2022

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


def get_line(fname, parno, lineno):
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


fname = input("Please file number ==> ") + ".txt"
parno = int(input("Please enter paragraph number ==> "))
lineno = int(input("Please enter the line number ==> "))
stop = False
file_text = ""

while (stop == False):
    line = get_line(fname, parno, lineno)
    line_parsed = parse_line(line)
    if (line == "END/0/0/0" or line_parsed == None):
        if (line_parsed == None):
            print("The wrong line was read")
        stop = True
    else:
        fname = str(line_parsed[0]) + ".txt"
        parno = line_parsed[1]
        lineno = line_parsed[2]
        file_text = file_text + line_parsed[3] + "\n"

print(file_text)
x = open("program.py", "w")
x.write(file_text)
x.close() 