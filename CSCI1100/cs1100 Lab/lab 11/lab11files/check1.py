# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 14:14:26 2022

@author: Emmanuel Usman
"""

class Ball(object):
    def __init__(self, x, y, dx, dy, radius, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color
        self.position = (self.x , self.y)
    def position(self):
        return self.position
    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dx
        self.position = (self.x , self.y)
    def bounding_box(self):
        
    def get_color(self):
        return self.color
        
        
        
        