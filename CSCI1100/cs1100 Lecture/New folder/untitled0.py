# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 14:55:21 2022

@author: Emmanuel Usman
"""
l1 =  [2, 3, 4, 4, 4, 5]
l2 = [1, 5, 6, 9]
l3 =  [ 6, 9, 13]


def merge(l1,l2,l3):
    L = []
    i1 = 0
    i2 = 0
    i3 = 0
    torf1 = False
    torf2 = False
    torf3 = False
    while not (torf1 and torf2 and torf3):
        if not torf1 and (torf2 or l1[i1] < l2[i2]) and (torf3 or l1[i1] < l3[i3]):
            L.append(l1[i1])
            i1+=1
            torf1 = i1>=len(l1)
            
        elif not torf2 and (torf3 or l2[i2] < l3[i3]):
            L.append(l2[i2])
            i2 += 1
            torf2 = i2 >= len(l2)
        else: 
            L.append(l3[i3])
            i3+=1
            torf3 = i3 >= len(l3)
    return L
print(merge(l1,l2,l3))

#3


scores =  [ 12, 90, 100, 52, 56, 76, 92, 83, 39, 77, 73, 70, 80 ]
'''
you need to create a case 
for lower bound values and upper bound
then you can simply use if statements 
to see which values are within your
lower bounds and upper and print using
formatting
'''
#8

def framed(name):
    if len(name) > len('hello!')+4:
        top = len(name)+4
        mid =round((top - len(name))/2)
        print('*' * top)
        print('*' + (" " * (mid-1)) + 'Hello!' + (' '* (mid-1)) + '*')
        print('*' + (" "*(mid-1))+ name +(" "*(mid-1)) + '*')
        print('*'*top)
    
framed('emmanuelllll')

#9
'''
file = 'blah.txt'
def getnames(city):
    f = open(file)
    count = 0
    for line in f:
        print(line)
        x = line.split('|')
        print(x)
        citystate = x[2].split(',')
        if city in citystate[1]:
            count+=1
    print(count)
    return count
getnames('Washington')
'''

#12

got = [ ['tyrion',9], ['cersei',3], ['jon',8], ['daenerys',5], ['arya',9], ['sansa',6], ['tywin',4]]

first = ['none',0]
second = ['noen',0]
for item in  got:
    if item[1] > first[1]:
        first = item
    elif item[1] > second[1]:
        second = item
    else:
        continue
print(first)
print(second)

#11
inp = '___a__b_cd__e f_g___h_'

#13
'''
import random
class Die(object):
    def __init__(self, sides):
        sides = int(sides)
        if sides < 1:
            sides = 1
        self.sides = sides
        self.roll()
    def roll(self):
# random.randint(a, b) returns a random value, x, where a <= x <= b
        self.value = random.randint(1, self.sides)
i = 0
count = 0
while i == 0:
    count+=1
    d1 = Die(6)
    d2 = Die(10)
    x = d1.roll()
    y = d2.roll()
    if x==1 and y == 1:
        print('took',count,'turns')
        i = 1
   
        
'''
   
'''
L =[("oldpegleg", 1), ("cow", 4), ("trout", 0), ("jellyfish", 0), ("student", 2)]
l1 = []
for tup in L: continue if tup[1] = 0  else: l1.append("{}".format(tup[0]*tup[1]))
'''
string = 'Monty Python'
l = list(string)
print(" ".join(l))
for num in range(len(l)):
    firstitem = l[0]
    lastindex = len(l)-1
    l.pop(0)
    l.insert(lastindex, firstitem)
    string = " ".join(l)
    print(string)
  
#6
class Sudoku(object):
    def __init__(self,l = 0):
        self.courds = l
        board  = []
        for row in range(9):
            rowforboard = []
            for col in range(9):
                rowforboard.append('.')
            board.append(rowforboard)
        self.board = board
    def Board(self):
        if self.courds == 0:
            print(self.board)
            return self.board
        else:
            for courd in self.courds:
                rowindex = courd[0]
                colindex = courd[1]
                stringrep = courd[2]
                self.board[rowindex][colindex] = stringrep
            print(self.board)
            return self.board

a = Sudoku()
b = Sudoku([(1, 2, '7'), (2, 5, '9')])
a.Board()
b.Board()

#7

inp = True
d = {'planks': 0, 'poles': 0, 'shingles': 0, 'sticks': 0}
while inp:
    dimensions = input("Enter the dimensions (l, w): ").strip()
    if dimensions == "":
        inp = False
        print("There were {} planks, {} poles, {} shingles, and {} sticks".format(d['planks'],d['poles'],d['shingles'],d['sticks']))
    else:
        dimensions = dimensions.split(',')
        dimensions[0] = int(dimensions[0])
        dimensions[1] = int(dimensions[1])
        if dimensions[0] >=4:
            board = 'long'
        else:
            board = 'short'
        if board == 'long' and dimensions[1] >= 5:
            board = 'plank'
            d['planks']+=1
        elif board == 'long' and dimensions[1] < 5:
            board = 'pole'
            d['poles']+=1
        elif board == 'short' and dimensions[1] >= 5:
            board = 'shingle'
            d['shingles'] +=1
        elif board == 'short' and dimensions[1] < 5:
            board = 'sticks'
            d['sticks']+=1     

number = input('Please enter an amount between 0 and 1 ==> ').strip()
number = float(number)
d = {'quarters': 0, 'dimes': 0, 'nickels': 0, 'pennies': 0}
if number >= 0.25 : 
    quarters = number//0.25
    number = number - (quarters*.25)
    d['quarters'] = quarters
if number >= .10:
    dimes = number // .1
    number = number - (dimes * .1)
    d['dimes'] = dimes
if number>= .5:
    nickels = number // .05
    number = number - (nickels * .05)
    d['nickels'] = nickels
if number >= .01:
    pennies = number // .01
    number = number - (pennies * .01)
    d['pennies'] = pennies

print('You need ==> 25 cent: {0:}   10 cent: {1:}   5 cent: {2:}   1 cent: {3:}'.format(d['quarters'], d['dimes'], d['nickels'], d['pennies']))


#4 test
def find_factors(val):
    if val <=0:
        return None
    else:
        num = val / 2
        factorlist = set()
        l = []
        for i in range(val):
            l.append(i)
        for number in l: 
            if val % num == 0:
                num2 = val / num
                if num < num2:
                    tup = (num, num2)
                else:
                    tup = (num2, num)
                factorlist.add(tup)
    return factorlist

print(find_factors(12))
                
    
    




