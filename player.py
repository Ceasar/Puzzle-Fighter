import grid
import gem
import rotate
import random
import math

PENALTY = 1
RANDOM = random.Random()

class Player(object):
    '''A player object.'''

    def __init__(self, topleft):
        self.grid = grid.Grid(topleft)
        self.rotate = rotate.build_random_rotate(self.grid)
        self.opponent = None

    def counter(self, number):
        '''Drops gem into the enemy grid.'''
        global PENALTY
        cols = range(grid.WIDTH)
        cols.remove(self.opponent.rotate.pivot.x)
        try: #Can't remove same num from cols twice.
            cols.remove(self.opponent.rotate.lever.x)
        except:
            pass
        total = 2 * number / 3 - PENALTY
        for num in range(total):
            col = RANDOM.choice(cols)
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

class AI(Player):
    def compute(self):
        best_theta = 0
        best_x = 0
        old_score = 0
        score = 0
        for i in range(0,3):
            theta = i*math.pi/2
            if not theta is math.pi: 
                for x in range(0, grid.WIDTH-1):
                    self.rotate.update_theta(theta)
                    self.rotate.move_to_x(x)
                    self.rotate.drop()
                    for gem in self.rotate.pivot.get_neighbors:
                        if gem.color is self.rotate.pivot.color:
                            score = score +1
                    for gem in self.rotate.lever.get_neighbors:
                        if gem.color is self.rotate.pivot.color:
                            score = score +1
                    if score > old_score:
                        best_theta = theta
                        best_x = x
        print best_theta
        print best_x
        return (best_theta, best_x) 
                
        
    def move(self, theta, x):
        while not self.rotate.theta is theta:
            self.rotate.rotate_clockwise()
        if x > self.rotate.pivot.x:
            while not x is self.rotate.pivot.x:
                self.rotate.move_right()
        elif x < self.rotate.pivot.x:
            while not x is self.rotate.pivot.x:
                self.rotate.move_left()
        self.rotate.drop()
        
    def move_old(self):
        roll = RANDOM.random()
        if roll > 0.90:
            self.rotate.drop()
        elif roll > 0.45:
            self.rotate.move_left()
        else:
            self.rotate.move_right()
        if roll > 0.66:
            self.rotate.rotate_clockwise()
        elif roll > 0.33:
            self.rotate.rotate_anticlockwise()
