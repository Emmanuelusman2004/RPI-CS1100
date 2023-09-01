# -*- coding: utf-8 -*-
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
    print(len(newstring))
    return newstring

string = "WRPI|WRPI is the campus radio station. We broadcast 365 days a year at 10,000 effective watts for up to 75 miles around RPI. Our studios are located on the first floor of the DCC. Our programming includes a wide range of alternative and experimental music, cultural and public affairs programs, live local bands, special events, and sports simulcasts."
print(get_words(string))