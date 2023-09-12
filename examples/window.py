#library
import pygame

#start pygame
pygame.init()

#setup window (W, D)
screen = pygame.display.set_mode([480, 480])

#start loop and setup quit condition
running = True
while running: 
    
    #check if user clicked to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #fill background (R, G, B)
    screen.fill((255, 255, 255))
    
    #draw circle (where, color(R, G, B), position(W, D), size(px))
    pygame.draw.circle(screen, (255, 0, 0), (240, 240), 80)
    
    #flip (update) the display
    pygame.display.flip()


#quit
pygame.quit()
