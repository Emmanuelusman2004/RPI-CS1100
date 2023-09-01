# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 14:35:03 2022

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

file1 = "csa.txt"
z = process(file1)


file2 = "allclubs.txt"
f = open(file2, "r")
listoflines = f.readlines()
f.close()

clubs = []
for n in listoflines:
    s = get_words(n)
    clubs.append(s)

similaritynumbers = []
for n in clubs:
    if z != n:
        similarities = z.intersection(n)
        similaritynumbers.append(len(similarities))

h = sorted(similaritynumbers)

numbersoftop5 = h[-5:]
indexesofsim = []
for n in similaritynumbers:
    if n in numbersoftop5:
        x = similaritynumbers.index(n)
        similaritynumbers.pop(x)
        similaritynumbers.insert(x,"'")
        indexesofsim.append(x)
names = []
for n in indexesofsim:
    clubsim = listoflines[n]
    g = clubsim.split("|")
    nameofclub = g[0]
    names.append(nameofclub)
print("clubs similar to csa:", end = " ")
for n in names:
    print(n + ",", end = " ")
print("")
print("")

file1 = "ea.txt"
z = process(file1)


file2 = "allclubs.txt"
f = open(file2, "r")
listoflines = f.readlines()
f.close()

clubs = []
for n in listoflines:
    s = get_words(n)
    clubs.append(s)

similaritynumbers = []
for n in clubs:
    if z != n:
        similarities = z.intersection(n)
        similaritynumbers.append(len(similarities))

h = sorted(similaritynumbers)

numbersoftop5 = h[-5:]
indexesofsim = []
for n in similaritynumbers:
    if n in numbersoftop5:
        x = similaritynumbers.index(n)
        similaritynumbers.pop(x)
        similaritynumbers.insert(x,"'")
        indexesofsim.append(x)

names = []
for n in indexesofsim:
    clubsim = listoflines[n]
    g = clubsim.split("|")
    nameofclub = g[0]
    names.append(nameofclub)

print("clubs similar to ea:", end = " ")
for n in names:
    print(n + ",", end = " ")
print("")
print("")




file1 = "kendo.txt"
z = process(file1)


file2 = "allclubs.txt"
f = open(file2, "r")
listoflines = f.readlines()
f.close()

clubs = []
for n in listoflines:
    s = get_words(n)
    clubs.append(s)

similaritynumbers = []
for n in clubs:
    if z != n:
        similarities = z.intersection(n)
        similaritynumbers.append(len(similarities))

h = sorted(similaritynumbers)

numbersoftop5 = h[-5:]
indexesofsim = []
for n in similaritynumbers:
    if n in numbersoftop5:
        x = similaritynumbers.index(n)
        similaritynumbers.pop(x)
        similaritynumbers.insert(x,"'")
        indexesofsim.append(x)
        
names = []
for n in indexesofsim:
    clubsim = listoflines[n]
    g = clubsim.split("|")
    nameofclub = g[0]
    names.append(nameofclub)

print("clubs similar to kendo:", end = " ")
for n in names:
    print(n + ",", end = " ")
print("")
print("")
