# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 22:52:31 2022

@author: Emmanuel Usman
"""

imdb_file = input("Enter the name of the IMDB file ==> ").strip()
counts = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1
appearances = []
name = []
for key in counts:
    appearances.append(counts[key])
    name.append(key)

most = max(appearances)
indexmostperson = appearances.index(most)
person = name[indexmostperson]
singlets = appearances.count(1)

print("{} appears most often: {} times".format(person, most))
print("{} people appear once".format(singlets))