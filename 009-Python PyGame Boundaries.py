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
lead_y_change = 0

clock = pygame.time.Clock()

while not gameExit:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = 10
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -10
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = 10
                lead_x_change - 0

    # Here logic of boundaries x and y on 800*600
    if lead_x >=800 or lead_x < 0 or lead_y >=600 or lead_y < 0:
        gameExit = True
        

    lead_x += lead_x_change
    lead_y += lead_y_change
    gameDisplay.fill(red)
    pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,10,10])
    pygame.display.update()

pygame.quit()
quit()
