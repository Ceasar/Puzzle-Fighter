import pygame
import random
import math
import gem
import grid

def build_random_rotate(gridx):
    print "built a random rotation object"
    
    pivot = gem.build_random_gem()
    lever = gem.build_random_gem()
    return Rotate(pivot,lever, gridx)

class Rotate:
    """Rotation class of an Object - this class rotates the2 block objects"""

    def __init__(self, pivot, lever,gridx):
        self.pivot = pivot 
        self.lever = lever
        self.theta = 0
        self.grid = gridx
        gridx.put(0,4,pivot)
        gridx.put(1,4,lever)

    def rotate_clockwise(self):
        if not self.is_dead():
            try:
                self.lever.set_xy(int(self.pivot.x + math.cos(self.theta)), int(self.pivot.y + math.sin(self.theta)))
                self.theta = math.pi/2 + self.theta
                if self.theta == math.pi*2: self.theta = 0

            except:
                self.pivot.set_xy(int(self.lever.x + math.cos(self.theta + math.pi)), int(self.lever.y + math.sin(self.theta + math.pi)))
                self.theta = self.theta + math.pi/2 
                if self.theta == math.pi*2: self.theta = 0

             
    def rotate_anticlockwise(self):
        if not self.is_dead():
            try:
                self.lever.set_xy(int(self.pivot.x - math.cos(self.theta)), int(self.pivot.y - math.sin(self.theta)))
                self.theta = self.theta - math.pi/2
                if self.theta == -math.pi*2: self.theta = 0

            except:
                self.pivot.set_xy(int(self.lever.x - math.cos(self.theta + math.pi)), int(self.lever.y - math.sin(self.theta + math.pi)))
                self.theta = math.pi/2 - self.theta
                if self.theta == math.pi*2: self.theta = 0


    def is_dead(self):
        return math.fabs(self.lever.x - self.pivot.x) + math.fabs(self.lever.y - self.pivot.y) > 1


    def move_right(self):
        try:
            righta = self.pivot.get_right()
            rightb = self.lever.get_right()
        except:
            return
        if righta is None or righta is self.lever:
            self.pivot.set_y(self.lever.x + 1)
        if rightb is None or rightb is self.lever:
            self.lever.set_y(self.pivot.x + 1)

    def move_left(self):
        try:
            lefta = self.pivot.get_left()
            leftb = self.lever.get_left()
        except:
            return
        if lefta is None or lefta is self.lever:
            self.pivot.set_y(self.lever.x - 1)
        if leftb is None or leftb is self.pivot:
            self.lever.set_y(self.pivot.x - 1)
            
    def update(self):
        ydiff = self.pivot.y - self.lever.y
        if ydiff > 0:
            self.pivot.lower()
            self.lever.lower()
        else:
            self.lever.lower()
            self.pivot.lower()

    def drop(self):
        self.pivot.quickdrop()
        self.lever.quickdrop()
        
    def draw(self, screen):
        global SIZE
        self.pivot.draw
        self.lever.draw
