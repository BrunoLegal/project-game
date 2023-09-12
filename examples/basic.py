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

#start pygame
pygame.init()

#set screen size as constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#create the screen object with the size of the previous constants
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


