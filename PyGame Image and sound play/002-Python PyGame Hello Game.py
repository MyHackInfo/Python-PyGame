import pygame,sys
pygame.init()
windowSize =(800,600)
screen = pygame.display.set_mode(windowSize)

myriadProFont = pygame.font.SysFont("Myriad pro",60)
helloGame = myriadProFont.render("Hello Game",1,(255,0,255),(255,255,255))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.blit(helloGame,(300,250))
    pygame.display.update()
