# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 13:17:27 2022

@author: Emmanuel Usman
"""
import json
import Bears
class Berryfield(object):
    def __init__(self, file):
        self.file = file
        f = open(self.file,'r')
        data = json.loads(f.read())
        self.berryfield = data['berry_field']
        self.copyofberryfield = data['berry_field']
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
        
    def surroundingobject(self,position):
        position = (position[0]-1,position[1]-1)
        x  = self.berryfield
        print(x)
        topleft = (0,0)
        topright = (0,len(x[0])-1)
        botleft = (len(x)-1,0)
        botright = (len(x)-1,len(x[0])-1)
        if position[1] == 0 and ((position != topleft) or (position != botleft)): 
            topobj = x[position[0]-1][position[1]]
            botobj = x[position[0]+1][position[1]]
            topright = x[position[0]-1][position[1]+1]
            rightobj = x[position[0]][position[1]+1]
            botright = x[position[0]+1][position[1]+1]
            surroundingobj = [topobj,botobj,topright,rightobj,botright]
        elif position[0] == 0 and ((position != topleft) or (position != topright)):
            leftobj = x[position[0]][position[1]-1]
            rightobj = x[position[0]][position[1]+1]
            botobj = x[position[0]+1][position[1]]
            botright = x[position[0]+1][position[1]+1]
            botleft = x[position[0]+1][position[1]-1]
            surroundingobj = [botleft,botobj,botright,leftobj,rightobj]
        elif position[1] == len(x[0]) and ((position != topright) or (position != botright)):
            topobj = x[position[0]-1][position[1]]
            botobj = x[position[0]+1][position[1]]
            topleft = x[position[0]-1][position[1]-1]
            leftobj = x[position[0]][position[1]-1]
            botleft = x[position[0]+1][position[1]-1]
            surroundingobj = [topobj,botobj,topleft,leftobj,botleft]
        elif position[0] == len(x) and ((position != botleft) or (position != botright)):
            leftobj = x[position[0]][position[1]-1]
            rightobj = x[position[0]][position[1]+1]
            topobj = x[position[0]-1][position[1]]
            topright = x[position[0]-1][position[1]+1]
            topleft = x[position[0]-1][position[1]-1]
            surroundingobj = [topleft,topobj,topright,leftobj,rightobj]
        elif position == topleft:
            rightobj = x[0][1]
            botobj = x[1][0]
            botrightobj = x[1][1]
            surroundingobj = [rightobj,botobj,botrightobj]
        elif position == topright:
            leftobj = x[0][len(x[0])-1]
            botleftobj = x[1][len(x[0])-1]
            botobj = x[1][len(x)]
            surroundingobj = [leftobj,botleftobj,botobj]
        elif position == botleft:
            topobj = x[len(x)-1][0]
            rightobj = x[len(x)][1]
            toprightobj = x[len(x)-1][1]
            surroundingobj = [topobj,rightobj,toprightobj]
        elif position == botright:
            topobj = x[len(x)-1][len(x[0])]
            leftobj = x[len(x)][len(x)-1]
            topleftobj = x[len(x)-1][len(x)-1]
            surroundingobj = [topobj,leftobj,topleftobj]
        else:
            topleftobj = x[position[0]-1][position[1]-1]
            topobj = x[position[0]-1][position[1]]
            toprightobj = x[position[0]-1][position[1]+1]
            leftobj = x[position[0]][position[1]-1]
            rightobj = x[position[0]][position[1]+1]
            botleftobj = x[position[0]+1][position[1]-1]
            botobj = x[position[0]+1][position[1]]
            botrightobj = x[position[0]+1][position[1]+1]
            surroundingobj = [topleftobj,topobj,toprightobj,leftobj,rightobj,botleftobj,botobj,botrightobj]
        print(x)
        return surroundingobj
        
    def growberry(self):
        print(self.berryfield)
        for row in range(len(self.berryfield)):
            for berry in range(len(self.berryfield[0])):
                if self.berryfield[row][berry] < 10 and self.berryfield[row][berry] > 1:
                    self.berryfield[row][berry] += 1
                    
    def spreadberry(self):
        for row in range(len(self.berryfield)):
            for berry in range(len(self.berryfield[0])):
                position = (row,berry)
                neighbors = self.surroundingobject(position)
                if neighbors.count(10) >= 1:
                    self.berryfield[row][berry] += 1
        
    def __str__(self):
        bf = self.copyofberryfield
        ab = self.activebears
        at = self.activetourists
        #set the courd for the bears
        for bear in ab:
            xcourd = bear[0]
            ycourd = bear[1]
            bf[xcourd][ycourd] = 'B'
        
        #set the courd for the tourists
        for tourist in at:
            xcourd = tourist[0]
            ycourd = tourist[1]
            if bf[xcourd][ycourd] == "B":
                bf[xcourd][ycourd] = "X"
            else:
                bf[xcourd][ycourd] = "T"
        
        string = ""
        for n in range(len(bf)):
            for s in range(len(bf[0])):
                g = bf[n][s]
                while len(str(g)) < 4:
                    g = " " + str(g)
                string = string + g
            if n != len(bf)-1:    
                string+=  "\n"
                
        print('Field has {0:} berries.'.format(self.allberries))
        print(string)
        print()
        print("Active Bears:")
        for bear in ab:
            print('Bear at ({0:},{1:}) moving {2:}'.format(bear[0],bear[1],bear[2]))
        print()
        print("Active Tourists:")
        for tourist in at:
            print('Tourist at ({0},{1}), 0 turns without seeing a bear.'.format(tourist[0],tourist[1]))
        
        
        