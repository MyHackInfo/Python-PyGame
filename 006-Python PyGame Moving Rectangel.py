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

lead_x = 300
lead_y = 300

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        # Here Keydown event for moving event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x -= 10
            if event.key == pygame.K_RIGHT:
                lead_x +=10

    gameDisplay.fill(red)
    # Here use rect for our obj for snake x or y position
    pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,10,10])
    pygame.display.update()


pygame.quit()
quit()
