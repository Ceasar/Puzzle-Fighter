import os, sys
import pygame
import pygame.locals
import grid
import gem
import random
import player
import threading
import time

class Updater(threading.Thread):
    '''Handles brick drop speed.'''
    def __init__(self, players):
        threading.Thread.__init__(self)
        self.daemon = True
        self.running = False
        self.players = players

    def run(self):
        self.running = True
        while self.running:
            for playerx in self.players:
                playerx.grid.update()
            print "waiting 1 second..."
            time.sleep(1)
            print "done waiting."

class Main:
    """The Main class of the Puzzle Fighter game - this class handles
    initialization and creation of the game"""

    def __init__(self, width=640, height=960):
        """Initialize"""
        self.size = width, height
        self.screen = pygame.display.set_mode(self.size)
        self.running = False
        topleft = (0, 0)
        topmid = (width / 2, 0)
        self.players = [player.Player(topleft), player.Player(topmid)]
        #Test
        self.players[0].grid.put(3, 0, gem.build_random_gem())
        self.players[0].grid.put(3, 2, gem.build_random_gem())
        self.players[0].grid.put(4, 0, gem.build_random_gem())
        self.players[1].grid.put(5, 6, gem.build_random_gem())

    def run(self):
        """Run the main loop of the game"""
        black = 0,0,0
        updater = Updater(self.players)
        updater.start()
        print "thread done."
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(black)
            for playerx in self.players:
                playerx.grid.draw(self.screen)
            pygame.display.flip()

    def counter(self, player, number):
        rand = random.Random
        for num in range(number):
            col = rand.randint(0, grid.WIDTH)
            gem = gem.build_random_gem()
            player.grid.insert_gem(0, col)
            gem.counter = True
            gem.fall()

if __name__ == "__main__":
    MainWindow = Main()
    MainWindow.run()
