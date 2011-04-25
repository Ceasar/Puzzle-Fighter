import grid
import gem
import rotate
import random
import math

PENALTY = 1

class Player(object):
    '''A player object.'''

    def __init__(self, topleft):
        self.grid = grid.Grid(topleft)
        self.rotate = rotate.build_random_rotate(self.grid)
        self.opponent = None

    def counter(self, number):
        '''Drops gem into the enemy grid.'''
        global PENALTY
        rand = random.Random()
        cols = range(grid.WIDTH)
        cols.remove(self.opponent.rotate.pivot.x)
        try: #Can't remove same num from cols twice.
            cols.remove(self.opponent.rotate.lever.x)
        except:
            pass
        total = 2 * number / 3 - PENALTY
        for num in range(total):
            col = rand.choice(cols)
            new_gem = gem.build_random_regular_gem()
            self.opponent.grid.put(0, col, new_gem)
            new_gem.counter = 5
            new_gem.quickdrop()

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
        total = 1 + exploded
        self.grid.update_dropped()
        while exploded > 0:
            exploded = self.grid.try_explode()
            total += exploded
            self.grid.update_dropped()
        self.counter(total)

    def check_rotate(self):
        '''Check to see if the rotate object is dead.'''
        if not self.rotate.is_alive():
            self.rotate.pivot.active = False
            self.rotate.lever.active =  False
            self.rotate = rotate.build_random_rotate(self.grid)

    def draw(self, screen):
        '''Draw the state of the game.'''
        self.grid.draw(screen)
