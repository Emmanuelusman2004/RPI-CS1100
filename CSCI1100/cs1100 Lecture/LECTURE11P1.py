# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 23:29:36 2022

@author: Emmanuel Usman
"""
def earlier_semester(x,y):
    if x[1] < y[1]:
        return "True"
    elif x[1] > y[1]:
        return "False"
    elif x[1] == y[1]:
        if x[0] == 'Spring' and y[0] == 'Fall':
            return "True"
        if x[0] == 'Spring' and y[0] == 'Spring':
            return "False"
        if x[0] == 'Fall' and y[0] == 'Spring':
            return 'False'


w1 = ('Spring',2015)
w2 = ('Spring',2014)
w3 = ('Fall', 2014)
w4 = ('Fall', 2015)
print( "{} earlier than {}? {}".format( w1, w2, earlier_semester(w1,w2)))
print( "{} earlier than {}? {}".format( w1, w1, earlier_semester(w1,w1)))
print( "{} earlier than {}? {}".format( w1, w4, earlier_semester(w1,w4)))
print( "{} earlier than {}? {}".format( w4, w1, earlier_semester(w4,w1)))
print( "{} earlier than {}? {}".format( w3, w4, earlier_semester(w3,w4)))
print( "{} earlier than {}? {}".format( w1, w3, earlier_semester(w1,w3)))
    