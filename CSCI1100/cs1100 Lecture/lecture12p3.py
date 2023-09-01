# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 14:04:59 2022

@author: Emmanuel Usman
"""
def find_min(Listoflists):
    listofmins = []
    for list_ in Listoflists:
        x = min(list_)
        listofmins.append(x)
    y = min(listofmins)
    return y
            
if __name__ == "__main__":
    v = [ [ 11,12,3], [6, 8, 4], [ 17, 2, 18, 14] ]
    print("Min of list v: {}".format(find_min(v)) )
    u = [ [ 'car', 'tailor', 'ball' ], ['dress'], ['can', 'cheese', 'ring' ], \
              [ 'rain', 'snow', 'sun' ] ]
    print("Min of list u: {}".format(find_min(u)) )