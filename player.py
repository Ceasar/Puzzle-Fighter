import grid
import gem
import rotate

class Player(object):
    '''A player object.'''

    def __init__(self, topleft):
        self.grid = grid.Grid(topleft)
        self.rotate = rotate.build_random_rotate(self.grid)

    def update(self):
        '''Update the state of the player.'''
        self.grid.update()
        self.check_rotate()

    def check_rotate(self):
        if not self.rotate.is_alive():
            self.rotate = rotate.build_random_rotate(self.grid)

    def draw(self, screen):
        '''Draw the state of the game.'''
        self.grid.draw(screen)
