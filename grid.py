import gem

HEIGHT = 5
WIDTH = 5

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

    def __init__(self):
        self.grid = build_matrix(HEIGHT, WIDTH)
        self.gems = []

    def update(self):
        '''Update all the gems in the grid.'''
        print "grid updating " + str(len(self.gems)) + " gems..."
        for gem in self.gems:
            gem.update()
        self.explode()

    def explode(self):
        '''Try to blow up the crash gem.'''
        for gem in self.gems:
            if gem.crash:
                exploded = gem.try_to_explode()
                if exploded:
                    self.update()

    def put(self, x, y, gem):
        '''Insert a gem.'''
        self.grid[y][x] = gem
        self.gems.append(gem)
        gem.grid = self.grid
        gem.x = x
        gem.y = y

    def move(self, x1, y1, x2, y2):
        '''Moves a gem from one spot to another.'''
        self.grid[y2][x2] = self.grid[y1][x1]
        self.grid[y1][x1] = None

    def draw(self, screen):
        '''Draws all the gems in the grid.'''
        for gem in self.gems:
            gem.draw(screen)

