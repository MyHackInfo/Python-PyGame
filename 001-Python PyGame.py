# Opne cmd And install PyGame
# pip install pygame

## PyGame ##
# It is module of python that use for create game
# in python and more detail go pygame.org

# first import pygame module
import pygame
pygame.init()
# g = pygame.init()
# print(g)

gameDisplay = pygame.display.set_mode((800,600))

# Both are some work
#pygame.display.flip()   # flip() use for all update
pygame.display.update() # update() use for certan area update

pygame.quit()
quit()
