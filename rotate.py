import pygame
import random
import math
import gem
import grid

def build_random_rotate(gridx):
    print "built a random rotation object"
    
    a = gem.build_random_gem()
    b = gem.build_random_gem()
    gridx.put(0,4,a)
    gridx.put(1,4,b)
    return Rotate(a,b)

class Rotate:
    """Rotation class of an Object - this class rotates the2 block objects"""

    def __init__(self, gem1, gem2):
        self.pivot = gem1 #pivot gem
        self.lever = gem2
        self.theta = 0

    def rotClock(self):
        if not self.isDead():
            try:
                self.lever.set_xy(int(self.pivot.x + math.cos(self.theta)), int(self.pivot.y + math.sin(self.theta)))
                self.theta = math.pi/2 + self.theta
                if self.theta == math.pi*2: self.theta = 0
                print self.lever.x
                print self.lever.y
                print self.pivot.x
                print self.pivot.y
            except:
                self.pivot.set_xy(int(self.lever.x + math.cos(self.theta + math.pi)), int(self.lever.y + math.sin(self.theta + math.pi)))
                self.theta = self.theta + math.pi/2 
                if self.theta == math.pi*2: self.theta = 0
                print self.lever.x
                print self.lever.y
                print self.pivot.x
                print self.pivot.y
             
    def rotCounterClock(self):
        if not self.isDead():
            try:
                self.lever.set_xy(int(self.pivot.x - math.cos(self.theta)), int(self.pivot.y - math.sin(self.theta)))
                self.theta = self.theta - math.pi/2
                if self.theta == -math.pi*2: self.theta = 0
                print self.lever.x
                print self.lever.y
                print self.pivot.x
                print self.pivot.y
            except:
                self.pivot.set_xy(int(self.lever.x - math.cos(self.theta + math.pi)), int(self.lever.y - math.sin(self.theta + math.pi)))
                self.theta = math.pi/2 - self.theta
                if self.theta == math.pi*2: self.theta = 0
                print self.lever.x
                print self.lever.y
                print self.pivot.x
                print self.pivot.y

    def isDead(self):
        if math.fabs(self.lever.x - self.pivot.x) + math.fabs(self.lever.y - self.pivot.y) > 1:
            return true
        else:
            return false

    def moveRight(self):
        try:
            righta = self.pivot.get_right()
            rightb = self.lever.get_right()
        except:
            return
        if righta is None or righta is self.lever:
            self.pivot.set_y(self.lever.x + 1)
        if rightb is None of rightb is self.lever:
            self.lever.set_y(self.pivot.x + 1)

    def moveLeft(self):
        try:
            lefta = self.pivot.get_left()
            lefta = self.lever.get_left()
        except:
            return
        if lefta is None or lefta is self.lever:
            self.pivot.set_y(self.lever.x - 1)
        if leftb is None or leftb is self.pivot:
            self.lever.set_y(self.pivot.x - 1)
            
    def update(self):
        try:
            belowa = self.pivot.get_below()
            belowb = self.lever.get_below()
        except:
            return
        if belowa is None or belowa is self.lever:
            self.pivot.set_y(self.lever.y + 1)
        if belowb is None or belowb is self.pivot:
            self.lever.set_y(self.pivot.y + 1)

    def drop(self):
        self.pivot.quickdrop()
        self.lever.quickdrop()
        
    def draw(self, screen):
        global SIZE
        self.pivot.draw
        self.lever.draw
