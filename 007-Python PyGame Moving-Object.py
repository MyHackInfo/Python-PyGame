import pygame
pygame.init()

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
lead_x_change = 0

# Use time.clock()
clock = pygame.time.Clock()

while not gameExit:
    # Here put time.clock for detect time frame per/sec.
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
            if event.key == pygame.K_RIGHT:
                lead_x_change = 10


    lead_x += lead_x_change
    gameDisplay.fill(red)
    pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,10,10])
    pygame.display.update()


pygame.quit()
quit()
