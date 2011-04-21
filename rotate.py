import pygame
import random

class Rotate:
    """Rotation class of an Object - this class rotates the2 block objects"""

    def __init__(self, gem1, gem2):
        self.gem1 = gem1 #pivot gem
        self.gem2 = gem2

    def rotClock(self):
        if(gem2.get_neighbors(0)==gem1):
            if(gem2.y <= 4):
                gem2.set_x(gem2.x - 1)
                gem2.set_y(gem2.y + 1)
            else:
                gem2.set_x(gem2.x - 1)
                gem1.set_y(gem1.y - 1)
        elif(gem2.get_neighbors(1)==gem1):
            if(gem2.y >=1):
                gem2.set_x(gem2.x + 1)
                gem2.set_y(gem2.y - 1)
            else:
                gem2.set_x(gem2.x + 1)
                gem1.set_y(gem1.y + 1)
        elif(gem2.get_neighbors(2)==gem1):
            if(gem2.x >=1):
                gem2.set_x(gem2.x - 1)
                gem2.set_y(gem2.y - 1)
            else:
                gem2.set_y(gem2.y - 1)
                gem1.set_x(gem1.x + 1)
        elif(gem2.get_neighbors(3)==gem1):
            if(gem2.x <= 4):
                gem2.set_x(gem2.x + 1)
                gem2.set_y(gem2.y + 1)
            else:
                gem2.set_y(gem2.y + 1)
                gem1.set_x(gem1.x - 1)
        else: raise Exception
             
    def rotCounterClock(self):
        if(gem2.get_neighbors(2)==gem1):
            if(gem2.x <= 4):
                gem2.set_x(gem2.x - 1)
                gem2.set_y(gem2.y + 1)
            else:
                gem2.set_y(gem2.y - 1)
                gem1.set_x(gem1.x - 1)
        elif(gem2.get_neighbors(3)==gem1):
            if(gem2.x >=1):
                gem2.set_x(gem2.x + 1)
                gem2.set_y(gem2.y - 1)
            else:
                gem2.set_y(gem2,y + 1)
                gem1.set_x(gem1.x + 1)
        elif(gem2.get_neighbors(0)==gem1):
            if(gem2.y >=1):
                gem2.set_x(gem2.x - 1)
                gem2.set_y(gem2.y - 1)
            else:
                gem2.set_x(gem2.x - 1)
                gem1.set_y(gem1.y + 1)
             
        elif(gem2.get_neighbors(1)==gem1):
            if(gem2.y <= 4):
                gem2.set_x(gem2.x + 1)
                gem2.set_y(gem2.y + 1)
            else:
                gem2.set_y(gem2.y - 1)
                gem1.set_x(gem1.x + 1)
        else: raise Exception

    def update(self):
        gem.set_y(gem
    
    def draw(self, screen):
        global SIZE
        pygame.draw.rect(screen, gem1.color, (gem1.x * SIZE, gem1.y * SIZE, (gem1.x + 1) * SIZE, (gem1.y - 1) * SIZE))
        pygame.draw.rect(screen, gem2.color, (gem2.x * SIZE, gem2.y * SIZE, (gem2.x + 1) * SIZE, (gem2.y - 1) * SIZE))
