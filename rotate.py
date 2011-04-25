import pygame
import random
import math
import gem
import grid

def build_random_rotate(gridx):
    "Build a random rotate object."
    pivot = gem.build_random_gem()
    lever = gem.build_random_gem()
    return Rotate(pivot, lever, gridx)

class Rotate:
    """Rotation class of an Object - this class rotates the2 block objects"""

    def __init__(self, pivot, lever, gridx):
        self.pivot = pivot
        self.lever = lever
        self.theta = 0
        self.grid = gridx
        gridx.put(1, 4, pivot)
        gridx.put(0, 4, lever)

    def rotate_clockwise(self):
        try:
            self.lever.set_xy(int(self.pivot.x + math.cos(self.theta)), int(self.pivot.y + math.sin(self.theta)))
            self.theta = math.pi/2 + self.theta
            if self.theta == math.pi*2: self.theta = 0
        except:
            self.pivot.set_xy(int(self.lever.x + math.cos(self.theta + math.pi)), int(self.lever.y + math.sin(self.theta + math.pi)))
            self.theta = self.theta + math.pi/2 
            if self.theta == math.pi*2: self.theta = 0
             
    def rotate_anticlockwise(self):
        try:
            self.lever.set_xy(int(self.pivot.x - math.cos(self.theta)), int(self.pivot.y - math.sin(self.theta)))
            self.theta = self.theta - math.pi/2
            if self.theta == -math.pi*2: self.theta = 0
        except:
            self.pivot.set_xy(int(self.lever.x - math.cos(self.theta + math.pi)), int(self.lever.y - math.sin(self.theta + math.pi)))
            self.theta = math.pi/2 - self.theta
            if self.theta == math.pi*2: self.theta = 0

    def is_dead(self):
        return math.fabs(self.lever.x - self.pivot.x) + math.fabs(self.lever.y - self.pivot.x) > 1

    def update(self):
<<<<<<< HEAD
        try:
            belowa = self.pivot.get_below()
            belowb = self.lever.get_below()
        except:
            return
        if belowa is None:
            self.pivot.set_y(self.lever.y + 1)
        if belowb is None:
            self.lever.set_y(self.pivot.y + 1)

    def drop(self):
        self.pivot.quickdrop()
        self.lever.quickdrop()
        
=======
        self.lever.set_y(self.lever.y + 1)
        self.pivot.set_y(self.lever.y + 1)
    
>>>>>>> c0ff68b9bcbac9c99d0fdbce1aa5da9f757deee1
    def draw(self, screen):
        self.pivot.draw(self.grid.topleft, screen)
        self.lever.draw(self.grid.topleft, screen)
