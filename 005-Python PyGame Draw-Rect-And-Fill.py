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

    gameDisplay.fill(red)
    # Here draw some rect using draw.rect()
    pygame.draw.rect(gameDisplay,black,[400,300,80,100])
    pygame.draw.rect(gameDisplay,green,[100,100,50,50])
    # Here draw some rect using fill() Its draw fast compare to rect
    gameDisplay.fill(blue, rect=[200,200,40,40])
    pygame.display.update()


pygame.quit()
quit()
