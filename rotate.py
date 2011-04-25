import pygame
import random
import math
import gem
import grid

def build_random_rotate(gridx):
    print "built a random rotation object"
    
    a = gem.build_random_gem()
    b = gem.build_random_gem()
    gridx.put(1,4,a)
    gridx.put(0,4,b)
    return Rotate(a,b)

class Rotate:
    """Rotation class of an Object - this class rotates the2 block objects"""

    def __init__(self, gem1, gem2):
        self.pivot = gem1 #pivot gem
        self.lever = gem2
        self.theta = 0

    def rotClock(self):
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

    def update(self):
        try:
            belowa = self.lever.get_below()
            belowb = self.pivot.get_below()
        except:
            return
        if below is None:
            self.lever.set_y(self.lever.y + 1)
            self.pivot.set_y(self.lever.y + 1)

    def drop(self):
        self.pivot.drop()
        self.lever.drop()
        
    def draw(self, screen):
        global SIZE
        pygame.draw.rect(screen, gem1.color, (gem1.x * SIZE, gem1.y * SIZE, (gem1.x + 1) * SIZE, (gem1.y - 1) * SIZE))
        pygame.draw.rect(screen, gem2.color, (gem2.x * SIZE, gem2.y * SIZE, (gem2.x + 1) * SIZE, (gem2.y - 1) * SIZE))
