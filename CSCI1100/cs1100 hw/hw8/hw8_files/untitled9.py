# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 13:17:27 2022

@author: Emmanuel Usman
"""
import json
class Berryfield(object):
    def __init__(self, file):
        self.file = file
        f = open(self.file,'r')
        data = json.loads(f.read())
        self.berryfield = data['berry_field']
        self.activebears =  data['active_bears']
        self.reservebears = data['reserve_bears']
        self.activetourists = data['active_tourists']
        self.reservetourists = data['reserve_tourists']
        
        #get all berries
        countofberries = 0
        for berrylist in self.berryfield:
            x = sum(berrylist)
            countofberries+=x
        self.allberries = countofberries
#        print(self.allberries)
        

        
    def __str__(self):
        #set the courd for the bears
        for bear in self.activebears:
            xcourd = bear[0]
            ycourd = bear[1]
            self.berryfield[xcourd][ycourd] = 'B'
        
        #set the courd for the tourists
        for tourist in self.activetourists:
            xcourd = tourist[0]
            ycourd = tourist[1]
            if self.berryfield[xcourd][ycourd] == "B":
                self.berryfield[xcourd][ycourd] = "X"
            else:
                self.berryfield[xcourd][ycourd] = "T"
        
        x = self.berryfield
        string = ""
        for n in range(len(x)):
            for s in range(len(x[0])):
                g = x[n][s]
                while len(str(g)) < 4:
                    g = " " + str(g)
                string = string + g
            if n != len(x)-1:    
                string+=  "\n"
        print('Field has {0:} Berries.'.format(self.allberries))
        print(string)
        
file = 'bears_and_berries_1.json'
test = Berryfield(file)
test.__str__()