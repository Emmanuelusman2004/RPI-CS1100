# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 22:10:34 2022

@author: Emmanuel Usman
"""

number1 = float(input("Enter the first number: "))
print(number1)
number2 = float(input("Enter the second number: "))
print(number2)
avg = (number1 + number2)/2

if (number1 > 10) and (number2 > 10):
    print("Both are above 10.")
    
elif (number1 < 10) and (number2 < 10):
    print("Both are below 10.")

print("Average is", "{:.2f}".format(avg))