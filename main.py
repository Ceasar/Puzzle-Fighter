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
                playerx.update()
            self.players[1].move()
            time.sleep(1)

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
        self.players = [player.Player(topleft), player.AI(topmid)]
        self.players[0].opponent = self.players[1]
        self.players[1].opponent = self.players[0]

    def handle_event(self, event):
        '''Handle key events.'''
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: #All for player[0]
            playerx = self.players[0]
            if event.key == pygame.K_RIGHT:
                playerx.rotate.rotate_clockwise()
            elif event.key == pygame.K_LEFT:
                playerx.rotate.rotate_anticlockwise()
            if event.key == pygame.K_d:
                playerx.rotate.move_right()
            elif event.key == pygame.K_a:
                playerx.rotate.move_left()
            if event.key == pygame.K_DOWN:
                playerx.rotate.drop()
            
    def run(self):
        """Run the main loop of the game"""
        black = 0,0,0
        updater = Updater(self.players)
        updater.start()
        self.running = True
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.screen.fill(black)
            for playerx in self.players:
                playerx.draw(self.screen)
            pygame.display.flip()

if __name__ == "__main__":
    MainWindow = Main()
    MainWindow.run()
