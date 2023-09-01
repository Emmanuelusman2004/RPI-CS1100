# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:49:52 2022

@author: Emmanuel Usman
"""

import json
import BerryField

class Bears(object):
    def __init__(self, row, column, direction, field):
        self.row = row - 1
        self.column = column -1
        self.direction = direction
        self.field = field
        self.berries = 0
    def outoffield(self):
        if self.row < 0 or self.column < 0 or self.row > len(self.field)-1 or self.column > len(self.field[0])-1:
            return True
    def move(self):
        if self.direction == 'N':
            self.berries = self.field[self.row][self.column]
            self.field[self.row][self.column] = 0
            self.row = self.row - 1
            self.berries+= self.field[self.row][self.column]
            self.field[self.row][self.column] = 0
            nextposition = (self.row,self.column)
            return nextposition
        elif self.direction == 'NE':
            self.berries = self.field[self.row][self.column]
            self.field[self.row][self.column] = 0
            self.row =self. row - 1
            self.column = self.column + 1
            self.berries+= self.field[self.row][self.column]
            self.field[self.row][self.column] = 0
            nextposition = (self.row,self.column)
            return nextposition
        elif self.direction == 'NW':
            self.berries = self.field[self.row][self.column]
            self.field[self.row][self.column] = 0
            self.row = self.row - 1
            self.column-=1
            self.berries+= self.field[self.row][self.column]
            self.field[self.row][self.column] = 0
            nextposition = (self.row,self.column)
            return nextposition
        elif self.direction == 'S':
            self.berries = self.field[self.row][self.column]
            self.field[self.row][self.column] = 0
            self.row+=1
            self.berries+= self.field[self.row][self.column]
            self.field[self.row][self.column] = 0
            nextposition = (self.row,self.column)
            return nextposition
        elif self.direction == 'SE':
            self.berries = self.field[self.row][self.column]
            self.field[self.row][self.column] = 0
            self.row+=1
            self.column+=1
            self.berries+= self.field[self.row][self.column]
            self.field[self.row][self.column] = 0
            nextposition = (self.row,self.column)
            return nextposition
        elif self.direction == 'SW':
            self.berries = self.field[self.row][self.column]
            self.field[self.row][self.column] = 0
            self.row+=1
            self.column-=1
            self.berries+= self.field[self.row][self.column]
            self.field[self.row][self.column] = 0
            nextposition = (self.row,self.column)
            return nextposition
        elif self.direction == 'W':
            self.berries = self.field[self.row][self.column]
            self.field[self.row][self.column] = 0
            self.column-=1
            self.berries+= self.field[self.row][self.column]
            self.field[self.row][self.column] = 0
            nextposition = (self.row,self.column)
            return nextposition
        elif self.direction == 'E':
            self.berries = self.field[self.row][self.column]
            self.field[self.row][self.column] = 0
            self.column+=1
            self.berries+= self.field[self.row][self.column]
            self.field[self.row][self.column] = 0
            nextposition = (self.row,self.column)
            return nextposition
    def moveandconsume(self):
        while self.berries != 30 and self.outoffield() != True:
            x = self.move()
            self.row = x[0]
            self.column = x[1]
            
        