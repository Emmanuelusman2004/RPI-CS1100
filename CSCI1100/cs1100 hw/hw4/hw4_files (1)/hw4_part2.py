# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 20:28:40 2022

@author: Emmanuel Usman
"""

import hw4_util
import sys

def retrievestate(state):
    w = hw4_util.part2_get_week(index)   #this function retrieves the state data and prints if there is no data for the state
    statefinder = 0
    for n in w:
        if n[0] == state:
            stats = n
            statefinder = 1
    if statefinder == 0 :
        print("State {0:} not found".format(state))
        return "none"
    return stats

def daily():
    state = input("Enter the state: ")
    print(state, end = "\n")
    stats = retrievestate(state)      #This function finds the avg for 100K using a proportion. 
    if stats == "none":
        return None
    totalcasesperweek = stats[2] + stats[3] + stats[4] + stats[5] + stats[6] + stats[7] + stats[8]
    avgcasesperdayforpop = (totalcasesperweek/7)
    avgcasesper100k = (avgcasesperdayforpop*100000)/stats[1]
    print("Average daily positives per 100K population: {0:.1f}".format(avgcasesper100k))

def quar(index):
    quarstates = []
    stateinfo =  hw4_util.part2_get_week(index)                 #for this function we copied the code to find the percent and avg per 100k to see which states were quarantined
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
    hw4_util.print_abbreviations(quarstates)
    
def pct():
    state = input("Enter the state: ")
    print(state, end = "\n")
    stats = retrievestate(state) #percent was a simple calculation which we retrieved the data and used a regular calculation
    if stats == "none":
        return None
    totaltestscasesperweek = sum(stats[2:16])
    poscases = sum(stats[2:9])
    pct = (poscases/totaltestscasesperweek)*100
    print("Average daily positive percent: {0:.1f}".format(pct))

def high(index):
    listofinfo = hw4_util.part2_get_week(index)
    averagesofstates = []
    for n in listofinfo:
        totalcasesperweek = sum(n[2:9])             #for all the states we find the average per 100k, round it and append it. After that we use the max to see which is the highest of them all.
        avgcasesperdayforpop = (totalcasesperweek/7)# We find the index of the highest to see what the index was for the"list of lists"(the directory of data) and therefore retrieve that data using the index and the stateletters for that.
        avgcasesper100k = (avgcasesperdayforpop*100000)/n[1]
        x = round(avgcasesper100k,1)
        averagesofstates.append(x)
    highavg = max(averagesofstates)
    indexofstate = averagesofstates.index(max(averagesofstates))
    stateletters = listofinfo[indexofstate][0]
    print("State with highest infection rate is {0:}".format(stateletters))
    print("Rate is {0:} per 100,000 people".format(highavg))

i = 0
while i < 10000:
    print("...")
    index = int(input("Please enter the index for a week: "))
    print(index, end = "\n")
    if index < 0:
        sys.exit()   #this is the loop which never ends hehe. Unless you enter a negative index which is this line. I had to import sys for this.
    elif index > 29:
        print("No data for that week")
    else:
        request = input("Request (daily, pct, quar, high): ")
        print(request)
        request = request.lower()
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
