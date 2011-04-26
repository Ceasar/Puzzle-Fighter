import grid
import gem
import rotate
import random
import math
import time

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
        '''updating the player for explosions'''
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
        '''computes best overall position for AI to move to each turn'''
        best_theta = 0
        best_x = 0
        best_score = 0
        
        for theta in [0, math.pi / 2, math.pi, 3 * math.pi / 2]:
            if theta == 0:
                start = 0
                end = grid.WIDTH - 1
            elif theta == (math.pi / 2 or 3 * math.pi / 2):
                start = 0
                end = grid.WIDTH
            else:
                start = 1
                end = grid.WIDTH
                
            good_score, good_theta, good_x = self.computation(theta, start, end)
            if good_score > best_score:
                best_score = good_score
                best_theta = good_theta
                best_x = good_x
        return best_theta, best_x
                

    def computation(self, theta, start, end):
        '''computes best score for each orientation of rotate object'''
        good_score = 0
        good_theta = 0
        good_x = 0
        orig_x_p = self.rotate.pivot.x
        orig_y_p = self.rotate.pivot.y
        orig_x_l = self.rotate.lever.x
        orig_y_l = self.rotate.lever.y
        orig_theta = self.rotate.theta
        
        for x in range(start, end):
            while not int(self.rotate.theta) == int(theta):
                self.rotate.rotate_anticlockwise()
            self.rotate.move_to_xy(x, self.rotate.pivot.y)
            self.rotate.drop()
            score = self.score()
            if score > good_score:
                good_score = score
                good_theta = theta
                good_x = x
            self.rotate.pivot.set_xy(orig_x_p, orig_y_p)
            self.rotate.lever.set_xy(orig_x_l, orig_y_l)
            self.rotate.theta = orig_theta
        return good_score, good_theta, good_x 
                

    def score(self):
        '''creates a score for each possible move of the AI'''s
        score = 0
        for gem in self.rotate.pivot.get_neighbors():
            if not gem is None:
                if gem.color == self.rotate.pivot.color:
                    if gem.crash:
                        score = score + 20
                    score = score + 6
                else:
                    score = score - 3
        for gem in self.rotate.lever.get_neighbors():
            if not gem is None:
                if gem.color == self.rotate.lever.color:
                    if gem.crash:
                        score = score + 20
                    score = score + 6
                else:
                    score = score - 3
        score = score + self.rotate.pivot.y + self.rotate.lever.y
        return score
        
    def move(self):
        '''moves the block for each move for the AI'''
        theta, x = self.compute()
        orig_theta = self.rotate.theta
        while not int(self.rotate.theta) == int(theta):
            self.rotate.rotate_clockwise()    
        if x > self.rotate.pivot.x:
            while not x == self.rotate.pivot.x:
                self.rotate.move_right()
                if self.rotate.pivot.x > grid.WIDTH:
                    break
        elif x < self.rotate.pivot.x:
            while not x == self.rotate.pivot.x:
                self.rotate.move_left()
                if self.rotate.pivot.x < 0:
                    break
        self.rotate.drop()
