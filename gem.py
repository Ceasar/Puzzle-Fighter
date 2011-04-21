import pygame
import random

SIZE = 10

COLORS = ['red', 'blue', 'yellow', 'green']
RGB_VALUES = {'red' : (255, 0, 0), 'blue' : (0, 0, 255), 'yellow' : (0, 255, 255), 'green' : (0, 255, 255)}
RANDOM = random.Random()
def build_random_gem():
    print "built a random gem"
    color = RANDOM.choice(COLORS)
    color = RGB_VALUES[color]
    roll = RANDOM.random()
    if roll > 0.90:
        crash = True
    else:
        crash = False
    return Gem(color, crash)

class Gem(object):
    '''Represents a gem object.'''
    def __init__(self, color, crash):
        self.color = color
        self.crash = crash
        self.x = 0 #refers to grid
        self.y = 0 #refers to grid
        self.grid = None
        self.fall_delay = 1000
        self.counter = False

    def get_neighbors(self):
        '''Get the adjcant gems.'''
        left = self.grid[self.x - 1][self.y]
        right = self.grid[self.x + 1][self.y]
        above = self.grid[self.x][self.y - 1]
        below = self.grid[self.x][self.y + 1]
        return [left, right, above, below]

    
    def fall(self):
        '''Lower the gem until it cannot fall anymore.'''
        try:
            print "trying to fall..."
            below = self.grid[self.x][self.y + 1]
            while below is None:
                print "below is empty..."
                self.y = self.y + 1
                print self.grid[self.x][self.y + 1]
                below = self.grid[self.x][self.y + 1]
                print "end reached"
                #sleep(self.fall_delay) #we'll need threading for this
        except:
            #Gem hit the bottom,so below should raise an exception.
            pass

    def update(self):
        '''Try to lower the gem.'''
        print "gem updating..."
        self.fall()
    
    def draw(self, screen):
        """Draws the gem"""
        global SIZE
        pygame.draw.rect(screen, self.color, (self.x * SIZE, self.y * SIZE, (self.x + 1) * SIZE, (self.y - 1) * SIZE))
        #pygame.draw.rect(pygame.display.surface, self.color,
        #(self.x * SIZE, self.y * SIZE, (self.x + 1) * SIZE, (self.y - 1) * SIZE))
        
    def try_to_explode(self):
        '''If the gem is a crash gem, try to explode it.'''
        if self.crash:
            for neighbor in self.get_neighbors():
                if neighbor.color == self.color:
                    self.explode()
                    return True

    def explode(self):
        '''Blows up the gem and nearby gems.'''
        self.grid.grid[self.x][self.y] = None
        self.grid.gems.remove(self)
        neighbors = self.get_neighbors()
        for neighbor in neighbors:
            if not neighbor is None and neighbor.color == self.color:
                exploded += 1 + neighbor.explode()
        return exploded
