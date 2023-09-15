import pygame
import random

#variable to change the speed
spd = 1

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
            self.rect.move_ip(0, -spd)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, spd)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-spd, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(spd, 0)
            
        #resets the position to the limit if the player tries to leave the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            
            
#Define the enemy object by extending pygame.sprite.Sprite
#The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center = (
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(1, 2)
        
    #Move the sprite based on speed
    #Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
       

#set screen size as constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 

#start pygame
pygame.init()

#create the screen object with the size of the previous constants
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

#Instantiate the player, it's just a rectangle for now
player = Player()

#Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

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
            
        #Add a new enemy
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
    
    #get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    #updates the player sprite based on user keypresses
    player.update(pressed_keys)
    
    enemies.update()
    
    #fills the screen with white
    screen.fill((0, 0, 0))
    
    #Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
        
    #checks if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        #if so, then remove the player and stop the loop
        player.kill()
        running = False
    
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



