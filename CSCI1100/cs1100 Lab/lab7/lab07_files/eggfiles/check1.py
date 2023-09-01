# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:03:20 2022

@author: Emmanuel Usman
"""

def parse_line(line):
    slashcount = line.count("/")
    splitline = line.split("/")
    y=''
    #print(splitline)
    if splitline[-1].isdigit() and splitline[-2].isdigit() and splitline[-3].isdigit():
        numlist = [splitline[-3],splitline[-2],splitline[-1]]
        splitline.pop(-1)
        splitline.pop(-1)
        splitline.pop(-1)
        if len(splitline) > 1:
            for n in splitline:
                x = splitline.index(n)
                y = y + splitline[x]
            tup = (int(numlist[0]),int(numlist[1]),int(numlist[2]),y)
        else:
            y = splitline[0]
            tup = (int(numlist[0]),int(numlist[1]),int(numlist[2]),y)
        return tup
    else:
        return None
        
    
    
    
    
    
    
    
    
print(parse_line("Here is some random text, like 5/4=3./12/3/4"))
print(parse_line("Here is some random text, like 5/4=3./12/3/4as"))
print(parse_line("Here is some random text, like 5/4=3./12/412/a/3/4"))
print(parse_line(" Here is some spaces 12/32/4"))
print(parse_line(" Again some spaces\n/12/12/12"))
