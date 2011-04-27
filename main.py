import os, sys
import pygame
import pygame.locals
import grid
import gem
import random
import player
import threading
import time

BLACK = 0, 0, 0

OFFSET = 70

pygame.init()

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
            time.sleep(1)

class AI (threading.Thread):
    '''Handles brick drop speed.'''
    def __init__(self, players, difficulty):
        threading.Thread.__init__(self)
        self.daemon = True
        self.running = False
        self.players = players
        self.difficulty = difficulty

    def run(self):
        self.running = True
        while self.running:
            self.players[1].move()
            time.sleep(self.difficulty)

class Main:
    """The Main class of the Puzzle Fighter game - this class handles
    initialization and creation of the game"""

    def __init__(self, width = 640, height = 600):
        global OFFSET
        self.size = width, height
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('PuzzleFighter!')
        self.running = False
        self.playing = True
        topleft = (OFFSET, 0)
        topmid = (width / 2 + OFFSET, 0)
        self.players = [player.Player(topleft), player.AI(topmid)]
        self.players[0].opponent = self.players[1]
        self.players[1].opponent = self.players[0]
        self.ai = None
        self.difficulty = 1.75
        self.updater = None
        self.winner = None
        self.loser = None
    
    def handle_event(self, event):
        '''Handle key events.'''
        if event.type == pygame.QUIT:
            sys.exit()
        if self.playing:
            if event.type == pygame.KEYDOWN: #All for player[0]
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
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    for playerx in self.players:
                        playerx.restart()
                    self.updater = Updater(self.players)
                    self.updater.start()
                    if self.winner == self.players[0]:
                        self.difficulty *= 0.9
                    else:
                        self.difficulty *= 1.1
                    self.ai = AI(self.players, self.difficulty)
                    self.ai.start()
                    self.playing = True

    def game_over(self):
        '''Handles the game over event.'''
        global BLACK
        self.playing = False
        self.ai.running = False
        self.updater.running = False
            
    def run(self):
        """Run the main loop of the game"""
        global BLACK, OFFSET
        self.updater = Updater(self.players)
        self.updater.start()
        self.ai = AI(self.players, self.difficulty)
        self.ai.start()
        self.running = True
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.screen.fill(BLACK)
            for playerx in self.players:
                playerx.draw(self.screen)
            if self.playing:
                for playerx in self.players:
                    if playerx.has_lost():
                        self.winner = playerx.opponent
                        self.loser = playerx
                        self.game_over()
            else:
                font = pygame.font.Font(None, gem.SIZE * 3)
                rfont = pygame.font.Font(None, 24)
                winner = font.render("WINNER", 1, (255, 255, 255))
                loser = font.render("LOSER", 1, (255, 255, 255))
                restart = rfont.render("Press 'r' to restart.", 1, (255, 255, 255))
                grid_height = grid.HEIGHT * gem.SIZE
                grid_width = grid.WIDTH * gem.SIZE
                wx = self.winner.grid.topleft[0]
                lx = self.loser.grid.topleft[0]
                self.screen.blit (winner, (wx - 30, grid_height / 4))
                self.screen.blit (loser, (lx - 10, grid_height / 4))
                self.screen.blit (restart, (OFFSET, grid_height + gem.SIZE))
                 
            pygame.display.flip()
        

if __name__ == "__main__":
    MainWindow = Main()
    MainWindow.run()
