# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 23:26:38 2022

@author: Emmanuel Usman
"""

def frame_string(word):
    x = len(word) + 6
    print('*' * x)
    print('**', word, '**')
    print('*' * x)

frame_string("Spanish Inquisition")
print("")
frame_string("Ni")