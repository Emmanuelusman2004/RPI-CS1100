# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 14:40:25 2022

@author: Emmanuel Usman
"""
number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
#if (number1 > 10 and number2 <= 10) or (number1 <= 10 and number2 > 10):
 #   print((number1 + number2)/2)
#elif (number1 > 10 and number2 > 10):
  #  print("Both are above 10")
 #   print((number1 + number2)/2)
#elif (number1 <= 10 and number2 <= 10):
 #   print("Both are below 10")
  #  print((number1 + number2)/2)
 


if (number1 > 10 and number2 <= 10) or (number1 <= 10 and number2 > 10):
    print((number1 + number2)/2)
elif (number1 > 10 and number2 > 10):
    print("Both are above 10")
    print((number1 + number2)/2)
elif (number1 <= 10 and number2 <= 10):
    print("Both are below 10")
    print((number1 + number2)/2)
    