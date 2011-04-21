import grid
import gem

class Player(object):
    '''A player object.'''

    def __init__(self):
        self.grid = grid.Grid()

    def update(self):
        '''Update the state of the player.'''
        self.grid.update()

    def explode(self):
        '''Check for any possible crashes.'''
        pass

    def draw(self):
        '''Draw the state of the game.'''
        self.grid.draw()
