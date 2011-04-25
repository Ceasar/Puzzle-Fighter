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
        return False
    def update(self):
        if theta == 0 or theta == math.pi:
            try:
                belowa = self.pivot.get_below()
            except:
                return
            if belowa is None:
                self.pivot.set_y(self.lever.y + 1)
            

    def drop(self):
        self.pivot.quickdrop()
        self.lever.quickdrop()
        
    def draw(self, screen):
        self.pivot.draw(self.grid.topleft, screen)
        self.lever.draw(self.grid.topleft, screen)
