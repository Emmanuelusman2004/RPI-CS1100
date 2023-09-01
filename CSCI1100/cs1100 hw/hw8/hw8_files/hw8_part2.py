# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:46:18 2022

@author: Emmanuel Usman
"""
import json
import BerryField
#import Tourists
#import Bears

if __name__ == "__main__":
    filename = input("Enter the json file name for the simulation => ").strip()
    print(filename)
    print("")
    
    print('Starting Configuration')
    x = BerryField.Berryfield(filename)
    x.str()
    touristsonfield = 100
    while touristsonfield != 0:
        x.growoberry()
        x.spreadberry()
#        x.movebears()
 #       x.reportbears()
  #      x.touristact()
   #     x.reporttoursist()
        x.str()
    

