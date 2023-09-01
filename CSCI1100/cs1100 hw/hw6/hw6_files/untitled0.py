# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 20:51:04 2022

@author: Emmanuel Usman
"""

countries = dict()
countries["Algeria"] =  37.1
countries["Canada"] = 34.9
countries["Uganda"] = 32.9
countries["Morocco"] = 32.7
countries["Sudan"] = 30.9
keylist = []
values = []
print(len(countries))
for key in countries:
    keylist.append(key)
    values.append(countries[key])
keylist.sort()
print(keylist)
values.sort()
print(values)