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
        '''rotate the object clockwise'''
        try:
            self.lever.set_xy(int(self.pivot.x + math.cos(self.theta)), int(self.pivot.y + math.sin(self.theta)))
        except:
            self.pivot.set_xy(int(self.lever.x + math.cos(self.theta + math.pi)), int(self.lever.y + math.sin(self.theta + math.pi)))
        self.theta = self.theta + math.pi/2 
        self.theta = self.theta % (2 * math.pi)

             
    def rotate_anticlockwise(self):
        '''rotate the object counter clockwise'''
        self.theta = math.pi/2 - self.theta
        self.theta = self.theta % (2 * math.pi)
        try:
            self.lever.set_xy(int(self.pivot.x - math.cos(self.theta)), int(self.pivot.y - math.sin(self.theta)))
        except:
            self.pivot.set_xy(int(self.lever.x - math.cos(self.theta + math.pi)), int(self.lever.y - math.sin(self.theta + math.pi)))
        


    def is_alive(self):
        '''checks if the object is still valid'''
        gems = [self.pivot, self.lever]
        for gem in gems:
            try:
                below = gem.get_below()
            except:
                return False
            if not (below is None or below in gems):
                return False
        return True

    def move_right(self):
        '''moves the object one space right'''
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
        '''moves the object one space left'''
        try:
            lefta = self.pivot.get_left()
            leftb = self.lever.get_left()
        except:
            return
        if lefta is None or lefta is self.lever:
            self.pivot.set_y(self.lever.x - 1)
        if leftb is None or leftb is self.pivot:
            self.lever.set_y(self.pivot.x - 1)

    def drop(self):
        '''quickly drops object into place'''
        self.pivot.quickdrop()
        self.lever.quickdrop()

