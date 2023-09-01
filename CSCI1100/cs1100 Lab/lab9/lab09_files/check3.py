# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 14:14:55 2022

@author: Emmanuel Usman
"""
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]
    
from Date import Date
cj = 0
cf = 0
cm = 0
ca = 0
cmay = 0
cjune = 0
cjuly = 0
caug = 0
csep = 0
coct = 0 
cnov = 0
cdec = 0
listofdatesobjects = []
f = open('birthdays.txt','r')
for line in f:
    line = line.strip()
    linezzz = line.split(" ")
    if int(linezzz[1]) == 1:
        cj+=1
    elif int(linezzz[1]) == 2:
        cf+=1
    elif int(linezzz[1]) == 3:
        cm+=1
    elif int(linezzz[1]) == 4:
        ca+=1
    elif int(linezzz[1]) == 5:
        cmay+=1
    elif int(linezzz[1]) == 6:
        cjune+=1
    elif int(linezzz[1]) == 7:
        cjuly+=1
    elif int(linezzz[1]) == 8:
        caug+=1
    elif int(linezzz[1]) == 9:
        csep+=1
    elif int(linezzz[1]) == 10:
        coct+=1
    elif int(linezzz[1]) == 11:
        cnov+=1
    elif int(linezzz[1]) == 12:
        cdec+=1
    d = Date(int(linezzz[0]),int(linezzz[1]),int(linezzz[2]))
    listofdatesobjects.append(d)
    
listofdatesobjects.sort()
print(listofdatesobjects[0])
print(listofdatesobjects[-1])

freq = [cj,cf,cm,ca,cmay,cjune,cjuly,caug,csep,coct,cnov,cdec]
indexoflargest = freq.index(max(freq)) + 1
print(month_names[indexoflargest])

































































