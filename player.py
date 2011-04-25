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
        self.rotate.update()
        if self.rotate.is_dead():
            self.rotate = rotate.build_random_rotate(self.grid)
        self.grid.update()

    def draw(self, screen):
        '''Draw the state of the game.'''
        self.rotate.draw(screen)
        self.grid.draw(screen)
