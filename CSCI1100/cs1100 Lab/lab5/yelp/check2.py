# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 13:24:23 2022

@author: Emmanuel Usman
"""

import lab05_util

restaurants = lab05_util.read_yelp('yelp.txt')
print(restaurants[0])
print("")

def evaluation(avgscore,reviews):
    if avgscore >= 0 and avgscore <= 2:
        print("This restaurant is rated bad, based on {0:} reviews.".format(reviews))
    elif avgscore > 2 and avgscore <= 3:
        print("This restaurant is rated average, based on {0:} reviews.".format(reviews))
    elif avgscore >3 and avgscore <=4:
        print("This restaurant is rated above average, based on {0:} reviews.".format(reviews))
    elif avgscore >4 and avgscore <=5:
        print("This restaurant is rated very good, based on {0:} reviews.".format(reviews))

def print_info(y):
    print(restaurants[y][0] + " (" + restaurants[y][5] + ")")
    x = restaurants[y][3].split("+")
    print("    " + x[0])
    print("    " + x[1])
    if len(restaurants[y][-1]) > 3:
        avgscore1 = (sum(restaurants[y][-1]) - max(restaurants[y][-1]) - min(restaurants[y][-1]))/(len(restaurants[y][-1]) - 2)
        print("Average Score: {0:.2f}".format(avgscore1))
        reviews = len(restaurants[y][-1]) - 2
        evaluation(avgscore1, reviews)
        print("")
    else:
        avgscore = sum(restaurants[y][-1])/len(restaurants[y][-1])
        print("Average Score: {0:.2f}".format(avgscore))
        reviews = len(restaurants[y][-1])
        evaluation(avgscore,reviews)
        print("")
i = 0 
while i < 100:    
    idnum = int(input("Please enter an id: "))
    print("")
    truid = idnum - 1
    print_info(truid)
    i +=1