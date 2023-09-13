import pygame

#import some keys coordinates from pygame.locals
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#Define a Player object by extending pygame.sprite.Sprite
#The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
    
    #move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
       

#set screen size as constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 

#start pygame
pygame.init()

#create the screen object with the size of the previous constants
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Instantiate the player, it's just a rectangle for now
player = Player()

#variable for main loop
running = True

#main loop
while running:
    #runs through every event that happened
    for event in pygame.event.get():
        #checks if the event type was a key being pressed 
        if event.type == KEYDOWN:
            #checks to see if the key that was pressed was Escape
            if event.key == K_ESCAPE:
                #kills the loop and closes
                running = False
        #checks if the window was closed        
        elif event.type == QUIT:
            #kills the loop
            running = False
    
    #get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    #updates the player sprite based on user keypresses
    player.update(pressed_keys)
    
    #fills the screen with white
    screen.fill((0, 0, 0))
    
    #Draws the player on the screen
    screen.blit(player.surf, player.rect)

    #creates a surface with the size of 50x50px
    ##surf = pygame.Surface((50, 50))
    #fills that surface with the color black
    ##surf.fill((0, 0, 0))
    ##rect = surf.get_rect()

    #time to draw stuff
    #these lines will draw surf on the center of the screen
    ##screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    ##pygame.display.flip()

    #stores the center of surf in a tuple
    ##surf_center = (
    ##    (SCREEN_WIDTH - surf.get_width())/2,
    ##    (SCREEN_HEIGHT - surf.get_height())/2
    ##)
    
    #updates new position
    ##screen.blit(surf, surf_center)
    pygame.display.flip()
