# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:19:49 2022

@author: Emmanuel Usman
"""

import json
import BerryField

if __name__ == "__main__":
#    filename = input("Enter the json file name for the simulation => ").strip()
#    print(filename)
#    print("")
    
    x = BerryField.Berryfield("bears_and_berries_1.json")
    x.__str__()
    x.growberry()
    x.spreadberry()
    x.__str__()