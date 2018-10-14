import pygame
pygame.init()

# Color combination
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Hunter")

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    # Here we use color for background of screen useing fill()
    gameDisplay.fill(red)
    pygame.display.update()


pygame.quit()
quit()
