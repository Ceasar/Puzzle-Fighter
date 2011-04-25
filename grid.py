import pygame
import gem

HEIGHT = 12
WIDTH = 6

def build_matrix(height, width):
    '''Builds an empty matrix.'''
    matrix = []
    for h in range(height):
        matrix.append([])
        for w in range(width):
            matrix[h].append(None)
    return matrix

class Grid(object):
    '''A grid object.'''

    def __init__(self, topleft):
        self.grid = build_matrix(HEIGHT, WIDTH)
        print self.grid
        self.gems = []
        self.topleft = topleft

    def update(self):
        '''Update all the gems in the grid.'''
        print "grid updating " + str(len(self.gems)) + " gems..."
        for row in reversed(self.grid):
            for gem in row:
                if not gem is None:
                    gem.update()
        self.explode()

    def explode(self):
        '''Try to blow up the crash gem.'''
        for gem in self.gems:
            if gem.crash:
                exploded = gem.try_to_explode()
                if exploded > 0:
                    self.update()

    def put(self, x, y, gem):
        '''Insert a gem.'''
        self.grid[y][x] = gem
        self.gems.append(gem)
        gem.grid = self.grid
        print x, y
        gem.x = x
        gem.y = y

    def move(self, x1, y1, x2, y2):
        '''Moves a gem from one spot to another.'''
        self.grid[y2][x2] = self.grid[y1][x1]
        self.grid[y1][x1] = None

    def draw(self, screen):
        '''Draws all the gems in the grid.'''
        pygame.draw.rect(screen, (255, 255, 255), self.topleft + (gem.SIZE * 6, gem.SIZE * 12), 1)
        for gemx in self.gems:
            gemx.draw(self.topleft, screen)
