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
        self.try_explode()

    def update_dropped(self):
        '''Update the dropped gems in the grid.'''
        for row in reversed(self.grid):
            for gem in row:
                if not gem is None and not gem.active:
                    gem.update()
        self.try_explode()

    def try_explode(self):
        '''Try to blow up the crash gem.'''
        for gem in self.gems:
            if gem.crash and not gem.active:
                exploded = self.try_to_explode(gem)
                if exploded > 0:
                    self.update_dropped()

    def try_to_explode(self, gem):
        '''If the gem is a crash gem, try to explode it.'''
        for neighbor in gem.get_neighbors():
            if not neighbor is None and neighbor.color == gem.color:
                if not neighbor.active:
                    return self.explode(gem)

    def explode(self, gem):
        '''Blows up the gem and nearby gems.'''
        self.remove(gem)
        neighbors = gem.get_neighbors()
        exploded = 0
        for neighbor in neighbors:
            if not neighbor is None and neighbor.color == gem.color:
                if not neighbor.active:
                    exploded += 1 + self.explode(neighbor)
        return exploded

    def put(self, y, x, gem):
        '''Insert a gem.'''
        self.grid[y][x] = gem
        self.gems.append(gem)
        gem.grid = self.grid
        gem.x = x
        gem.y = y

    def remove(self, gem):
        '''Removes a gem.'''
        print gem
        self.grid[gem.y][gem.x] = None
        self.gems.remove(gem)

    def move(self, x1, y1, x2, y2):
        '''Moves a gem from one spot to another.'''
        self.grid[y2][x2] = self.grid[y1][x1]
        self.grid[y1][x1] = None

    def draw(self, screen):
        '''Draws all the gems in the grid.'''
        pygame.draw.rect(screen, (255, 255, 255), self.topleft + (gem.SIZE * 6, gem.SIZE * 12), 1)
        for gemx in self.gems:
            gemx.draw(self.topleft, screen)
