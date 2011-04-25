import pygame
import random
import math
import gem
import grid

def build_random_rotate(gridx):
    '''Builds a random rotate object.'''
    pivot = gem.build_random_gem()
    lever = gem.build_random_gem()
    while pivot.color == lever.color and (pivot.crash or lever.crash):
        lever = gem.build_random_gem()
    return Rotate(pivot,lever, gridx)

class Rotate:
    """Rotation class of an Object - this class rotates the2 block objects"""

    def __init__(self, pivot, lever ,gridx):
        self.pivot = pivot 
        self.lever = lever
        self.theta = math.pi
        self.grid = gridx
        gridx.put(0,3,pivot)
        gridx.put(1,3,lever)
        pivot.active = True
        lever.active = True

    def rotate_clockwise(self):
        '''rotate the object clockwise'''
        try:
            a = self.pivot.x + int(math.cos(self.theta))
            b = self.pivot.y + int(math.sin(self.theta))
            self.lever.set_xy(a, b)
        except:
            c = self.lever.x + int(math.cos(self.theta + math.pi))
            d = self.lever.y + int(math.sin(self.theta + math.pi))
            self.pivot.set_xy(c, d)
        self.theta = self.theta + math.pi/2 
        self.theta = self.theta % (2 * math.pi)

             
    def rotate_anticlockwise(self):
        '''rotate the object counter clockwise'''
        try:
            a = self.pivot.x - int(math.cos(self.theta))
            b = self.pivot.y - int(math.sin(self.theta))
            try:
                self.lever.cond_set_xy(a, b)
            except:
                try:
                    self.lever.cond_set_xy(a+1, b)
                    self.pivot.cond_set_xy(a+2, b)
                except:
                    self.pivot.cond_set_xy(a,b+1)
                    self.lever.cond_set_yx(a,b+2)

        except:
            c = self.lever.x - int(math.cos(self.theta + math.pi))
            d = self.lever.y - int(math.sin(self.theta + math.pi))
            try:
                self.pivot.cond_set_xy(c, d)
            except:
                try:
                    self.pivot.cond_set_xy(a+1,b)
                    self.lever.cond_set_xy(a+2,b)
                except:
                    self.pivot.cond_set_xy(a,b+1)
                    self.lever.cond_set_xy(a,b+2)
        self.theta = self.theta + 3*math.pi/2
        self.theta = self.theta % (2 * math.pi)


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
        x_diff = self.pivot.x - self.lever.x
        if x_diff == -1:
            try:
                right = self.lever.get_right()
            except:
                return
            if right is None:
                self.lever.set_x(self.lever.x + 1)
                self.pivot.set_x(self.pivot.x + 1)
        if x_diff == 0:
            try:
                right_pivot = self.pivot.get_right()
                right_lever = self.lever.get_right()
            except:
                return
            if right_pivot is None and right_lever is None:
                self.pivot.set_x(self.pivot.x + 1)
                self.lever.set_x(self.lever.x + 1)
        if x_diff == 1:
            try:
                right = self.pivot.get_right()
            except:
                return
            if right is None:
                self.pivot.set_x(self.pivot.x + 1)
                self.lever.set_x(self.lever.x + 1)
                
    def move_left(self):
        '''moves the object one space left'''
        x_diff = self.pivot.x - self.lever.x
        if x_diff == 1:
            try:
                left = self.lever.get_left()
            except:
                return
            if left is None:
                self.lever.set_x(self.lever.x - 1)
                self.pivot.set_x(self.pivot.x - 1)
        if x_diff == 0:
            try:
                left_pivot = self.pivot.get_left()
                left_lever = self.lever.get_left()
            except:
                return
            if left_pivot is None and left_lever is None:
                self.pivot.set_x(self.pivot.x - 1)
                self.lever.set_x(self.lever.x - 1)
        if x_diff == -1:
            try:
                left = self.pivot.get_left()
                print left
            except:
                return
            if left is None:
                self.pivot.set_x(self.pivot.x - 1)
                self.lever.set_x(self.lever.x - 1)
    def drop(self):
        '''quickly drops object into place'''
        x_diff = self.pivot.x - self.lever.x
        y_diff = self.pivot.y - self.lever.y
        if x_diff is 0 and y_diff is -1:
            self.lever.quickdrop()
            self.pivot.quickdrop()
        else:
            self.pivot.quickdrop()
            self.lever.quickdrop()
        self.pivot.active = False
        self.lever.active =  False
