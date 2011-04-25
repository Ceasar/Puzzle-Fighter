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
        neighbors = []
        try:
            neighbors.append(self.grid[self.y][self.x - 1])
        except:
            pass
        try:
            neighbors.append(self.grid[self.y][self.x + 1])
        except:
            pass
        try:
            neighbors.append(self.grid[self.y - 1][self.x])
        except:
            pass
        try:
            neighbors.append(self.grid[self.y + 1][self.x])
        except:
            pass
        return neighbors

    def get_below(self):
        '''Get the gem below.'''
        return self.grid[self.y + 1][self.x]

    def get_above(self):
        '''Get the gem above.'''
        return self.grid[self.y - 1][self.x]

    def get_left(self):
        '''Get the gem on the left.'''
        if self.x-1 <0:
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

    def set_xy(self, x, y):
        """sets position of x and y"""
        self.move(self.x, self.y, x, y)
        self.x = x
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

    def quickdrop(self):
        while self.lower():
            self.lower()

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
            
    def try_to_explode(self):
        '''If the gem is a crash gem, try to explode it.'''
        for neighbor in self.get_neighbors():
            if not neighbor is None and neighbor.color == self.color:
                return self.explode()

    def explode(self):
        '''Blows up the gem and nearby gems.'''
        self.grid.remove(self.y, self.x, self)
        neighbors = self.get_neighbors()
        for neighbor in neighbors:
            if not neighbor is None and neighbor.color == self.color:
                exploded += 1 + neighbor.explode()
        return exploded
