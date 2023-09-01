# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 14:06:36 2022

@author: Emmanuel Usman
"""
import random
import time


def closest1(l):
    '''
    >>> L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
    >>> closest1(L1)
    (5.4, 4.3)
    '''
    if len(l) < 2:
        return (None,None)
    closestdist = abs(l[0] - l[1])
    closesttup = ()
    for firstnum in l:
        for secondnum in l:
            if firstnum == secondnum:
                continue
            distance = abs(secondnum - firstnum)
            if distance < closestdist:
                closestdist = distance
                closesttup = (firstnum,secondnum)
    return closesttup



def closest2(l):
    '''
    >>> L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
    >>> closest2(L1)
    (5.4, 4.3)
    '''
    newl = sorted(l)
    diff = abs(newl[0] - newl[1])
    tuppy = ()
    for num in range(len(newl) -1):
        index = num + 1
        diff2 = abs(newl[index] - newl[num])
        if diff2 < diff:
            diff = diff2
            tuppy = (newl[index],newl[num])
    return tuppy
        



if __name__ == '__main__':
    L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
    (x,y) = closest1(L1)
    print(x, y)
    
    L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
    (x,y) = closest2(L1)
    print(x, y)
    print("TEST LIST LEN 1000")
    test1 = []
    for n in range(1000):
        test1.append(random.uniform(0.0,1000.0))
    t1 = time.time()
    (x,y) = closest1(test1)
    t2 = time.time()
    print('Runtime ', str(t2 - t1))
    print(x, y)
    t1 = time.time()
    (x,y) = closest2(test1)
    t2 = time.time()
    print('Runtime ', str(t2 - t1))
    print(x, y)
    print("TEST LEN LIST 10000")
    test2 = []
    for n in range(10000):
        test2.append(random.uniform(0.0,1000.0))
    t1 = time.time()
    (x,y) = closest1(test2)
    t2 = time.time()
    print('Runtime ', str(t2 - t1))
    print(x, y)
    t1 = time.time()
    (x,y) = closest2(test2)
    t2 = time.time()
    print('Runtime ', str(t2 - t1))
    print(x, y)
    print('TEST LEN LIST 100')
    test3 = []
    for n in range(100):
        test3.append(random.uniform(0.0,100.0))
    t1 = time.time()
    (x,y) = closest1(test3)
    t2 = time.time()
    print('Runtime ', str(t2 - t1))
    print(x, y)
    t1 = time.time()
    (x,y) = closest2(test3)
    t2 = time.time()
    print('Runtime ', str(t2 - t1))
    print(x, y)
    

    
    