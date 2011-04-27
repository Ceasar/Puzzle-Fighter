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
    return Rotate(pivot, lever, gridx)

class Rotate:
    """Rotation class of an Object - this class rotates the2 block objects"""

    def __init__(self, pivot, lever, gridx):
        """creates the rotate object"""
        self.pivot = pivot 
        self.lever = lever
        self.theta = math.pi
        self.grid = gridx
        gridx.put(0, 3, pivot)
        gridx.put(1, 3, lever)
        pivot.active = True
        lever.active = True

    def update_theta(self, angle):
        """updates angle theta for rotate object"""
        self.theta = self.theta + angle 
        self.theta = self.theta % (2 * math.pi)
        
    
    def rotate_clockwise(self):
        '''rotate the object clockwise'''
        x = self.pivot.x + int(math.cos(self.theta))
        y = self.pivot.y + int(math.sin(self.theta))
        try:
            if x < 0 or y < 0:
                raise Exception
            future_pos = self.grid.grid[y][x]
            if future_pos is None:
                self.lever.set_xy(x,y)
                self.update_theta(math.pi / 2)
        except:
            x = self.lever.x + int(math.cos(self.theta + math.pi))
            y = self.lever.y + int(math.sin(self.theta + math.pi))
            self.pivot.set_xy(x, y)
            self.update_theta(math.pi/2)

    def rotate_anticlockwise(self):
        '''rotate the object counter clockwise'''
        x = self.pivot.x - int(math.cos(self.theta))
        y = self.pivot.y - int(math.sin(self.theta))
        try:
            if x < 0 or y < 0:
                raise Exception
            future_pos = self.grid.grid[y][x]
            if future_pos is None:
                self.lever.cond_set_xy(x, y)
                self.update_theta(3 * math.pi / 2)    
        except:
            x = self.lever.x - int(math.cos(self.theta + math.pi))
            y = self.lever.y - int(math.sin(self.theta + math.pi))
            self.pivot.set_xy(x, y)
            self.update_theta(3 * math.pi / 2)
            
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
            except:
                return
            if left is None:
                self.pivot.set_x(self.pivot.x - 1)
                self.lever.set_x(self.lever.x - 1)

    def move_to_xy(self, x, y):
        """moves rotate object to specific x, y position"""
        x_diff = self.pivot.x - self.lever.x
        y_diff = self.pivot.y - self.lever.y
        if x_diff == 1:
            try:
                self.lever.set_x(x - 1)
                self.pivot.set_x(x)
            except:
                pass
        elif x_diff == 0:
            try:
                self.pivot.set_x(x)
                self.lever.set_x(x)
            except:
                pass
        elif x_diff == -1:
            try:
                self.lever.set_x(x + 1)
                self.pivot.set_x(x)
            except:
                pass
        if y_diff == 1:
            try:
                self.lever.set_y(y - 1)
                self.pivot.set_y(y)
            except:
                pass
        elif y_diff == 0:
            try:
                self.pivot.set_y(y)
                self.lever.set_y(y)
            except:
                pass
        elif y_diff == -1:
            try:
                self.lever.set_y(y + 1)
                self.pivot.set_y(y)
            except:
                pass
                
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

    def aidrop(self):
        '''quickly drops object into place'''
        x_diff = self.pivot.x - self.lever.x
        y_diff = self.pivot.y - self.lever.y
        if x_diff is 0 and y_diff is -1:
            self.lever.quickdrop()
            self.pivot.quickdrop()
        else:
            self.pivot.quickdrop()
            self.lever.quickdrop()
