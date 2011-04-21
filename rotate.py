import pygame
import random

SIZE = 10

class Rotate:
    """Rotation class of an Object - this class rotates the2 block objects"""

    def __init__(self, gem1, gem2):
        self.gem1 = gem1 #pivot gem
        self.gem2 = gem2

    def rotClock(self):
        if(gem2.get_neighbors(0)==gem1):
            gem2.set_x(gem2.x - 1)
            gem2.set_y(gem2.y + 1)
        elif(gem2.get_neighbors(1)==gem1
            gem2.set_x(gem2.x + 1)
            gem2.set_y(gem2.y - 1)
        elif(gem2.get_neighbors(2)==gem1
            gem2.set_x(gem2.x - 1)
            gem2.set_y(gem2.y - 1)
        elif(gem2.get_neighbors(3)==gem1
            gem2.set_x(gem2.x + 1)
            gem2.set_y(gem2.y + 1)
        else raise Exception
             
    def rotCounterClock(self):

    def update(self):
        
    def draw(self, screen):
        global SIZE
        pygame.draw.rect(screen, self.color, (self.x * SIZE, self.y * SIZE, (self.x + 1) * SIZE, (self.y - 1) * SIZE))
