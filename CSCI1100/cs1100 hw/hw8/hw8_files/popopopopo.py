# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:05:26 2022

@author: Emmanuel Usman
"""

import json
import Bears
import copy
class Berryfield(object):
    def __init__(self, file):
        self.file = file
        f = open(self.file,'r')
        self.data = json.loads(f.read())
    #    print(self.data)
        self.berryfield = self.data['berry_field']
        self.copyofberryfield = self.data['berry_field']
        self.activebears =  self.data['active_bears']
        self.reservebears = self.data['reserve_bears']
        self.activetourists = self.data['active_tourists']
        self.reservetourists = self.data['reserve_tourists']
        self.bearsthatleft = []
        
    def growberry(self):
   #      print(self.berryfield)
         for row in range(len(self.berryfield)):
             for berry in range(len(self.berryfield[0])):
                 if self.berryfield[row][berry] < 10 and self.berryfield[row][berry] > 1:
                     self.berryfield[row][berry] += 1
         self.data["berry_field"] = self.berryfield
  #       print(self.data)
 #        print(self.berryfield)
#         print("after growth")

    def surroundingobject(self,position):
        position = (position[0]-1,position[1]-1)
        x  = self.berryfield
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
        return surroundingobj
    
    def spreadberry(self):
#        print("thos")
 #       print(self.berryfield)
        for row in range(len(self.berryfield)):
            for berry in range(len(self.berryfield[0])):
                if self.berryfield[row][berry] != 0:
                    continue
                position = (row,berry)
                neighbors = self.surroundingobject(position)
                if neighbors.count(10) >= 1:
                    self.berryfield[row][berry] += 1 
        self.data["berry_field"] = self.berryfield
#        print(self.data['berry_field'])
#        print(self.berryfield)

#I need to change the position of active bears to the new positions from new stuff so that the str fucntio
#works out and then I need to start on the toursist part. Before that i need to see if the bears are actually moving
#ask masha if the tourists leave if they see bears at the end of the iteration of if they count as the bears are moving
#also create a condition that prevents the bears from moving out of the area!

    def bearmove(self):
        for bear in self.activebears:
            x = Bears.Bears(bear[0],bear[1],bear[2],self.berryfield)
            x.moveandconsume()
            
    
    def __str__(self):
        bf = copy.deepcopy(self.data["berry_field"])
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
        
        if self.bearsthatleft != []:
            for bear in self.bearsthatleft:
                print(bear)
            
        string = ""
        for n in range(len(bf)):
            for s in range(len(bf[0])):
                g = bf[n][s]
                while len(str(g)) < 4:
                    g = " " + str(g)
                string = string + g
            if n != len(bf)-1:    
                string+=  "\n"
                
#        print('Field has {0:} berries.'.format(self.allberries))
        print(string)
        print()
        print("Active Bears:")
        for bear in ab:
            print('Bear at ({0:},{1:}) moving {2:}'.format(bear[0],bear[1],bear[2]))
        print()
        print("Active Tourists:")
        for tourist in at:
            print('Tourist at ({0},{1}), 0 turns without seeing a bear.'.format(tourist[0],tourist[1]))

x = Berryfield("bears_and_berries_1.json")
x.__str__()
x.growberry()
x.spreadberry()
x.bearmove()
#x.__str__()

#x.bearmove()



