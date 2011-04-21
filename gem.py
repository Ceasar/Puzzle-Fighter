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
        crash = False
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
        left = self.grid[self.y][self.x - 1]
        right = self.grid[self.y][self.x + 1]
        above = self.grid[self.y - 1][self.x]
        below = self.grid[self.y + 1][self.x]
        return [left, right, above, below]

    def get_below(self):
        '''Get the gem below.'''
        return self.grid[self.y + 1][self.x]

    def get_above(self):
        '''Get the gem above.'''
        return self.grid[self.y - 1][self.x]

    def get_left(self):
        '''Get the gem on the left.'''
        return self.grid[self.y][self.x - 1]

    def get_right(self):
        '''Get the gem on the right.'''
        return self.grid[self.y][self.x + 1]

    def set_x(x):
        '''Set the x position.'''
        self.move(self.x, self.y, x, self.y)
        self.x = x

    def set_y(y):
        '''Set the y position.'''
        self.move(self.x, self.y, self.x, y)
        self.y = y

    def move(self, x1, y1, x2, y2):
        '''Moves a gem from one spot to another.'''
        self.grid[y2][x2] = self.grid[y1][x1]
        self.grid[y1][x1] = None

    def drop(self, x, y1, y2):
        '''Drops a gem from one spot to another.'''
        self.grid[y2][x] = self.grid[y1][x]
        self.grid[y1][x] = None

    def update(self):
        '''Try to lower the gem.'''
        self.lower()

    def lower(self):
        '''Lowers the gem one row.'''
        try:
            below = self.get_below()
        except:
            return
        if not below is None:
            self.set_y(self.y - 1)
    
    def draw(self, screen):
        """Draws the gem"""
        global SIZE
        topleft = (self.x * SIZE, self.y * SIZE)
        pygame.draw.rect(screen, self.color, topleft + (SIZE, SIZE))
            
    def try_to_explode(self):
        '''If the gem is a crash gem, try to explode it.'''
        if self.crash:
            for neighbor in self.get_neighbors():
                if neighbor.color == self.color:
                    self.explode()
                    return True

    def explode(self):
        '''Blows up the gem and nearby gems.'''
        self.grid.grid[self.y][self.x] = None
        self.grid.gems.remove(self)
        neighbors = self.get_neighbors()
        for neighbor in neighbors:
            if not neighbor is None and neighbor.color == self.color:
                exploded += 1 + neighbor.explode()
        return exploded
