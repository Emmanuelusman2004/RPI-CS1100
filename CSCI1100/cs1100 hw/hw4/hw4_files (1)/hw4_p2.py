# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 20:28:40 2022

@author: Emmanuel Usman
"""

import hw4_util
import sys

def retrievestate(state):
    w = hw4_util.part2_get_week(index)
    statefinder = 0
    for n in w:
        if n[0] == state:
            stats = n
            statefinder = 1
    if statefinder == 0 :
        print("State {0:} not found".format(state))
    return stats

def daily():
    state = input("Enter the state: ")
    print(state, end = "\n")
    stats = retrievestate(state)    
    totalcasesperweek = stats[2] + stats[3] + stats[4] + stats[5] + stats[6] + stats[7] + stats[8]
    avgcasesperdayforpop = (totalcasesperweek/7)
    avgcasesper100k = (avgcasesperdayforpop*100000)/stats[1]
    print("Average daily positives per 100k population: {0:.1f}".format(avgcasesper100k))

def quar(index):
    quarstates = []
    stateinfo =  hw4_util.part2_get_week(index)
    for n in stateinfo:
        totalcasesperweek = n[2] + n[3] + n[4] + n[5] + n[6] + n[7] + n[8]
        avgcasesperdayforpop = (totalcasesperweek/7)
        avgcasesper100k = (avgcasesperdayforpop*100000)/n[1]
        #below is percent calculation
        totaltestscasesperweekforpct = sum(n[2:16])
        poscasesforpct = sum(n[2:9])
        pct = (poscasesforpct/totaltestscasesperweekforpct)*100
        if avgcasesper100k > 10 or pct > 10:
            quarstates.append(n[0])
    print("Quarantine states:")
    #i = 1
    #print(quarstates[0], end = " ")
    #while i < len(quarstates):
    #    if i % 10 == 0:
    #        print(quarstates[i], end = "\n")
    #    else:
    #        print(quarstates[i], end = " ")
    #    i+=1
    print(quarstates[0], end = " ")
    for s in quarstates:
        if quarstates.index(s) % 10 == 0 and quarstates.index(s) != 0:
            print(s, end = "\n")
        elif quarstates.index(s) == (len(quarstates) -1):
            print(s, end = "\n")
        else:
            print(s, end = " ")

def pct():
    state = input("Enter the state:")
    print(state, end = "\n")
    stats = retrievestate(state)
    totaltestscasesperweek = sum(stats[2:16])
    poscases = sum(stats[2:9])
    pct = (poscases/totaltestscasesperweek)*100
    print("Average daily positive percent: {0:.1f}".format(pct))

def high(index):
    listofinfo = hw4_util.part2_get_week(index)
    averagesofstates = []
    for n in listofinfo:
        totalcasesperweek = sum(n[2:9])
        avgcasesperdayforpop = (totalcasesperweek/7)
        avgcasesper100k = (avgcasesperdayforpop*100000)/n[1]
        x = round(avgcasesper100k,1)
        averagesofstates.append(x)
    highavg = max(averagesofstates)
    indexofstate = averagesofstates.index(max(averagesofstates))
    stateletters = listofinfo[indexofstate][0]
    print("State with the highest infection rate is {0:}".format(stateletters))
    print("Rate is {0:} per 100,000 people".format(highavg))

i = 0
while i < 10000:
    print("...")
    index = int(input("Please enter the index for a week: "))
    print(index, end = "\n")
    if index > 29 or index < 0:
        sys.exit()
    request = input("Request (daily, pct, quar, high): ")
    print(request)
    if request == "daily":  
        daily()
    elif request == "pct":
        pct()
    elif request == "quar":
        quar(index)
    elif request == "high":
        high(index)
    else:
        print("Unrecognized request")
