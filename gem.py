import pygame
import random
import time
import threading

SIZE = 30

COLORS = ['red', 'blue', 'yellow', 'green']
RGB_VALUES = {'red' : (255, 0, 0), 'blue' : (0, 0, 255), 'yellow' : (255, 255, 0), 'green' : (0, 255, 0)}
RANDOM = random.Random()
def build_random_gem():
    color = RANDOM.choice(COLORS)
    color = RGB_VALUES[color]
    roll = RANDOM.random()
    if roll > 0.80:
        crash = True
    else:
        crash = False
    return Gem(color, crash)

def build_random_regular_gem():
    color = RANDOM.choice(COLORS)
    color = RGB_VALUES[color]
    return Gem(color, False)

class Gem(object):
    '''Represents a gem object.'''
    def __init__(self, color, crash):
        self.color = color
        self.crash = crash
        self.x = 0 #refers to grid
        self.y = 0 #refers to grid
        self.grid = None
        self.active = False
        self.counter = 0

    def get_neighbors(self):
        '''Get the adjcant gems.'''
        try:
            above = self.get_above()
        except:
            above = -1
        if above != -1:
            yield above
        try:
            below = self.get_below()
        except:
            below = -1
        if below != -1:
            yield below
        try:
            right = self.get_right()
        except:
            right = -1
        if right != -1:
            yield right
        try:
            left = self.get_left()
        except:
            left = -1
        if left != -1:
            yield left

    def get_below(self):
        '''Get the gem below.'''
        return self.grid[self.y + 1][self.x]

    def get_above(self):
        '''Get the gem above.'''
        if self.y - 1 < 0:
            raise Exception
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
        try:
            self.move(self.x, self.y, x, self.y)
            self.x = x
        except:
            pass

    def set_y(self, y):
        '''Set the y position.'''
        try:
            self.move(self.x, self.y, self.x, y)
            self.y = y
        except:
            pass

    def cond_set_xy(self, x, y):
        if not self.grid[y][x] is None:
            raise Exception
        else:
            self.move(self.x, self.y, x, y)
            self.x = x
            self.y = y

    def set_xy(self, x, y):
        """sets position of x and y"""
        try:
            self.move(self.x, self.y, x, y)
            self.x = x
            self.y = y
        except:
            pass
            
    def move(self, x1, y1, x2, y2):
        '''Moves a gem from one spot to another.'''
        if x1<0 or y1 <0 or x2 <0 or y2 <0:
            raise Exception
        if x1 == x2 and y1 == y2:
            raise Exception
        if not self.grid[y2][x2] == None:
            raise Exception
        self.grid[y2][x2] = self.grid[y1][x1]
        self.grid[y1][x1] = None

    def update(self):
        '''Try to lower the gem.'''
        if self.active:
            self.lower()
        else:
            self.quickdrop()
        if self.counter > 0:
            self.counter = self.counter - 1

    def quickdrop(self):
        '''Drops the gem to the bottom.'''
        while self.lower():
            pass

    def lower(self):
        '''Lowers the gem one row.'''
        try:
            below = self.get_below()
        except:
            return False
        if below is None:
            try:
                self.set_y(self.y + 1)
            except:
                return False
            return True
    
    def draw(self, grid_offset, screen):
        """Draws the gem"""
        global SIZE
        topleft = (grid_offset[0] + self.x * SIZE,  grid_offset[1] + self.y * SIZE)
        color = self.color
        if self.counter > 0:
            color = (self.color[0] / self.counter, self.color[1] / self.counter, self.color[2] / self.counter)
        if self.crash:
            mid = (topleft[0] + SIZE / 2, topleft[1] + SIZE / 2)
            pygame.draw.circle(screen, color, mid, SIZE/ 2)
        else:
            pygame.draw.rect(screen, color, topleft + (SIZE, SIZE))
        if self.counter > 0:
            botright = (topleft[0] + SIZE, topleft[1] + SIZE)
            pygame.draw.line(screen, (0, 0, 0), topleft, botright)
            topright = (topleft[0] + SIZE, topleft[1])
            botleft = (topleft[0], topleft[1] + SIZE)
            pygame.draw.line(screen, (0, 0, 0), topright, botleft)
            
