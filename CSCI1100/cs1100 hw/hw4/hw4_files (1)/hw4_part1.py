# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 12:29:10 2022

@author: Emmanuel Usman
"""
import hw4_util
#we need to evaluate the amount of points for the length,case,digits,punctuation,
#NYlisence, and see if we reduce points for it being the same as a common password
#We make functions for each of these and then a loop for all of them.
#there is an order we need to think about to see which makes the operations easier
#first imports,functions,loops, then we have our print statements
#I need to try to make unique variable names and also make parameters and variable names not the same
def length(passcode): #this calculates the points you get for the length of the code and prints it
    L = len(passcode)
    if L == 6 or L == 7:
        points = 1
        print("Length: +1")
    elif L == 8 or L == 9 or L == 10:
        points = 2
        print("Length: +2")
    elif L > 10:
        points = 3
        print("Length: +3")
    else:
        points = 0
    return points

def case(passc,points):
    letters = passc.strip() #here we calculate the points off the cases
    capletters = []         #lists to append the upper case letters and lower case letters
    lowletters = []
    for n in letters:
        if n.isupper():  #goes through every character in the split list of the password and appends if its capitalized
            capletters.append(n)
        else:
            lowletters.append(n)
    if len(lowletters) >= 2 and len(capletters) >= 2:   #here we add points based on the possible combinations of cases
        points = points + 2
        print('Cases: +2')
    elif len(lowletters) == 1 and len(capletters) == 1:
        points = points + 1
        print('Cases: +1')
    elif len(lowletters) >= 1 and len(capletters) == 1:
        points = points + 1
        print('Cases: +1')
    elif len(lowletters) == 1 and len(capletters) >= 1:
        points = points + 1
        print('Cases: +1')
    else:
        points = points
    return points
    
def digits(password,points):
    all_numbers = ["0","1","2","3","4","5","6","7","8","9"]
    pas = password.strip()            #this area we calculate the points
    all_numbers_count= 0              #based off whether it has digits
    for n in pas:                     #we go through the split password and 
        if n in all_numbers:          #count the number of digits by seeing if it contains a character in the all_numbers list
            all_numbers_count+=1
    if all_numbers_count >= 2:
        points = points + 2
        print("Digits: +2")
    elif all_numbers_count == 1:
        points = points + 1
        print("Digits: +1")
    return points

def punctuation(password,points):
    punctuation2 = ["!","@","#","$"] #similar to what we did in digits we find
    punctuation1 = ["%","^","&","*"] #the split password go through it all in
    p = password.strip()             #loop and count how much is there and add it depending on which one we read
    countpunct2 = 0
    countpunct1 = 0
    for n in p:
        if n in punctuation2:       #these if statements determine if we add 1 pt or 2 pts
            countpunct2+= 1
        if n in punctuation1:
            countpunct1+= 1
    if countpunct2 >= 1:
        points = points + 1
        print("!@#$: +1")
    elif countpunct1 >= 1:
        points = points + 1
        print("%^&*: +1")
    return points

def NYlisence(password,points):
    p = password
    if len(p) == 7:
        listofletters = []
        listofnumbers = []             #we have different lists to put the
        strlist = p.split()            #letters and numbers if the list
        print(strlist)
        strlist = p[0:3]               #turns out to be 3 letters and 4
        strlist = strlist.lower()      #numbers we subtract 2 points
        intlist = p[3:7]
        if strlist.isalpha() == True:
            listofletters.append(strlist)
        if intlist.isdigit() == True:
            listofnumbers.append(intlist)
        if len(listofletters[0]) == 3 and len(listofnumbers[0]) == 4:
            points = points - 2
            print("License: -2")
    return points

def commonpassword(password,points):
    password = password.lower()
    hw4_util.part1_get_top()              #Here we use the function to retireve the list of cokmmon passwords and if "n" in the list of passwords is equal to a password we subract 3 points from the total points
    for n in hw4_util.part1_get_top():
        if password == n:
            points = points - 3
            print("Common: -3")
    return points

def points(password):
    lpoints = length(password)    #this function calls all the functions and adds up all the points for the combined score
    cpoints = case(password,lpoints)
    dpoints = digits(password,cpoints)
    ppoints = punctuation(password,dpoints)
    nylpoints = NYlisence(password,ppoints)
    cppoints = commonpassword(password,nylpoints)
    total_points = cppoints
    print("Combined score: {0:}".format(total_points))
    return total_points

def evaluation(password): #this function tidies up all the functions and provides an evalutaion wiht if statements
    p= points(password)
    if p <= 0:
        print("Password is rejected")
    elif p == 1 or p == 2:
        print("Password is poor")
    elif p == 3 or p == 4:
        print ("Password is fair")
    elif p == 5 or p == 6:
        print("Password is good")
    elif p >=7:
        print("Password is excellent")
    
password = input("Enter a password => ")
print(password)

evaluation(password)
