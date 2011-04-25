import pygame
import random

SIZE = 30

COLORS = ['red', 'blue', 'yellow', 'green']
RGB_VALUES = {'red' : (255, 0, 0), 'blue' : (0, 0, 255), 'yellow' : (255, 255, 0), 'green' : (0, 255, 255)}
RANDOM = random.Random()
def build_random_gem():
    print "built a random gem"
    color = RANDOM.choice(COLORS)
    color = RGB_VALUES[color]
    roll = RANDOM.random()
    if roll > 0.80:
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
        self.fast_fall = False
        self.counter = False

    def get_neighbors(self):
        '''Get the adjcant gems.'''
        try:
            yield self.grid[self.y][self.x - 1]
        except:
            pass
        try:
            yield self.grid[self.y][self.x + 1]
        except:
            pass
        try:
            yield self.grid[self.y - 1][self.x]
        except:
            pass
        try:
            yield self.grid[self.y + 1][self.x]
        except:
            pass

    def get_below(self):
        '''Get the gem below.'''
        return self.grid[self.y + 1][self.x]

    def get_above(self):
        '''Get the gem above.'''
        return self.grid[self.y - 1][self.x]

    def get_left(self):
        '''Get the gem on the left.'''
        if self.x - 1 < 0:
            raise Exception
        return self.grid[self.y][self.x - 1]

    def get_right(self):
        '''Get the gem on the right.'''
        return self.grid[self.y][self.x + 1]

    def set_x(self, x):
        '''Set the x position.'''
        self.move(self.x, self.y, x, self.y)
        self.x = x

    def set_y(self, y):
        '''Set the y position.'''
        self.move(self.x, self.y, self.x, y)
        self.y = y

    def cond_set_xy(self, x, y):
        if not self.grid[y][x] is None:
            raise Exception
        else:
            self.move(self.x, self.y, x, y)
            self.x = x
            self.y = y

    def set_xy(self, x, y):
        """sets position of x and y"""
        self.move(self.x, self.y, x, y)
        self.x = x
        self.y = y
            
    def move(self, x1, y1, x2, y2):
        '''Moves a gem from one spot to another.'''
        if x1<0 or y1 <0 or x2 <0 or y2 <0:
            raise Exception
        self.grid[y2][x2] = self.grid[y1][x1]
        self.grid[y1][x1] = None

    def update(self):
        '''Try to lower the gem.'''
        if self.fast_fall:
            self.quickdrop()
        else:
            self.lower()

    def quickdrop(self):
        while self.lower():
            pass

    def lower(self):
        '''Lowers the gem one row.'''
        print "lowering " + str(self.y)
        try:
            below = self.get_below()
        except:
            return False
        if below is None:
            self.set_y(self.y + 1)
            return True
    
    def draw(self, grid_offset, screen):
        """Draws the gem"""
        global SIZE
        topleft = (grid_offset[0] + self.x * SIZE,  grid_offset[1] + self.y * SIZE)
        if self.crash:
            mid = (topleft[0] + SIZE / 2, topleft[1] + SIZE / 2)
            pygame.draw.circle(screen, self.color, mid, SIZE/ 2)
        else:
            pygame.draw.rect(screen, self.color, topleft + (SIZE, SIZE))
