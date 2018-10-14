import pygame,sys
pygame.init()
windowSize =(800,600)
screen = pygame.display.set_mode(windowSize)

myriadProFont = pygame.font.SysFont("Myriad pro",60)
helloGame = myriadProFont.render("Hello Game",1,(255,0,255),(255,255,255))

helloGameSize = helloGame.get_size()
directionX ,directionY= 1,1

x,y = 0,0
clock = pygame.time.Clock()


while 1:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill((0,0,0))


    mousePosition = pygame.mouse.get_pos()
    x,y = mousePosition

    if x + helloGameSize[0] > 800:
        x = 800 - helloGameSize[0]

    if y + helloGameSize[1] > 600:
        y = 600 - helloGameSize[1]

    screen.blit(helloGame,(x,y))
    pygame.display.update()
