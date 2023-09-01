# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 14:16:14 2022

@author: Emmanuel Usman
"""

"""
Created on Wed Nov  2 13:03:45 2022

@author: Emmanuel Usman
"""

def get_words(string):
    a = string.replace("."," ")
    b = a.replace("("," ")
    c = b.replace(")"," ")
    d = c.replace('"'," ")
    e = d.replace(","," ")
    g = e.replace("|"," ")
    f = g.lower()
    newstring = set()
    splitdesc = f.split(" ")
    for n in splitdesc:
        if n == " " or n == "":
            continue
        if n.isalpha():
            if len(n) >= 4:
                newstring.add(n)
    return newstring

def process(file):
    f = open(file, "r")
    s = f.readlines()
    f.close()
    firstline = s[0]
    stringset = get_words(firstline)
    return stringset

file1 = 'wrpi.txt'
file2 = 'csa.txt'
set1 = process(file1)
set2 = process(file2)

compare1 = set1.difference(set2)
compare2 = set2.difference(set1)
compare = set1.intersection(set2)
print(compare)
print("")

print("Unique to wrpi: " + str(compare1))
print("")
print("Unique to csa " + str(compare2))

    