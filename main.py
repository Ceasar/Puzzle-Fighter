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
            for player in self.players:
                player.grid.update()
            time.sleep(1)

class Main:
    """The Main class of the Puzzle Fighter game - this class handles
    initialization and creation of the game"""

    def __init__(self, width=640, height=480):
        """Initialize"""
        self.size = width, height
        self.screen = pygame.display.set_mode(self.size)
        self.running = False
        #self.surface = pygame.get_surface()
        self.players = [player.Player(), player.Player()]
        #Test
        for playerx in self.players:
            playerx.grid.put(4, 0, gem.build_random_gem())

    def run(self):
        """Run the main loop of the game"""
        black = 0,0,0
        updater = Updater(self.players)
        updater.run()
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(black)
            for player in self.players:
                player.grid.draw(self.screen)
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
