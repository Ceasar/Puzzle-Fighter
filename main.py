import os, sys
import pygame
import pygame.locals
import grid
import gem
import random
import player

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
        """Main Loop of the game"""
        black = 0,0,0
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(black)
            for player in self.players:
                player.grid.update()
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

##    def LoadArraySpace(self):
##        """Load the initial sprite blocks that we need"""
##        global array
##     
##        array = Array()
##        self.snake_sprites = pygame.sprite.RenderPlain((self.snake))
##        
##        """figure out how many pellets we can display"""
##        nNumHorizontal = int(self.width/64)
##        nNumVertical = int(self.height/64)       
##        """Create the Pellet group"""
##        self.pellet_sprites = pygame.sprite.Group()
##        """Create all of the pellets and add them to the 
##        pellet_sprites group"""
##        for x in range(nNumHorizontal):
##            for y in range(nNumVertical):
##                self.pellet_sprites.add(Pellet(pygame.Rect(x*64, y*64, 64, 64)))



class Array(object):
    """This is our snake that will move around the screen"""
    
    def __init__(self):
        pass
        
    def move(self, key):
        """Move your self in one of the 4 directions according to key"""
        """Key is the pyGame define for either up,down,left, or right key
        we will adjust outselfs in that direction"""
##        xMove = 0;
##        yMove = 0;
##        
##        if (key == K_RIGHT):
##            xMove = self.x_dist
##        elif (key == K_LEFT):
##            xMove = -self.x_dist
##        elif (key == K_UP):
##            yMove = -self.y_dist
##        elif (key == K_DOWN):
##            yMove = self.y_dist
##        #self.rect = self.rect.move(xMove,yMove);
##        self.rect.move_ip(xMove,yMove);

if __name__ == "__main__":
    MainWindow = Main()
    MainWindow.run()
