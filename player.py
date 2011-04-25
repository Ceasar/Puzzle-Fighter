import grid
import gem
import rotate
import random

class Player(object):
    '''A player object.'''

    def __init__(self, topleft):
        self.grid = grid.Grid(topleft)
        self.rotate = rotate.build_random_rotate(self.grid)
        self.opponent = None

    def counter(self, number):
        rand = random.Random
        for num in range(number):
            col = rand.randint(0, grid.WIDTH)
            gem = gem.build_random_gem()
            self.opponent.grid.insert_gem(0, col)
            gem.counter = True
            gem.fall()

    def has_lost(self):
        '''Checks to see if a player has lost.'''
        for gem in self.grid.gems:
            if not gem.active and gem.y < 3:
                return True
        return False

    def update(self):
        '''Update the state of the player.'''
        self.grid.update()
        self.update2()

    def update2(self):
        self.check_rotate()
        exploded = self.grid.try_explode()
        self.grid.update_dropped()
        while exploded > 0:
            exploded = self.grid.try_explode()
            self.grid.update_dropped()

    def check_rotate(self):
        '''Check to see if the rotate object is dead.'''
        if not self.rotate.is_alive():
            self.rotate.pivot.active = False
            self.rotate.lever.active =  False
            self.rotate = rotate.build_random_rotate(self.grid)

    def draw(self, screen):
        '''Draw the state of the game.'''
        self.grid.draw(screen)
