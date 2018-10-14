import pygame,sys
pygame.init()
pygame.mixer.init()
windowSize =(800,600)
screen = pygame.display.set_mode(windowSize)


helloGame = pygame.image.load("PS circle.png")
helloGameSize = helloGame.get_size()
pygame.mouse.set_visible(0)

sound = pygame.mixer.Sound("Pluralsight.wav")

x,y = 0,0
directionX ,directionY= 1,1
clock = pygame.time.Clock()


while 1:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x += 5
            if event.key == pygame.K_LEFT:
                x -=5

            if event.key == pygame.K_DOWN:
                y +=5
            if event.key == pygame.K_UP:
                y -=5

    screen.fill((0,0,0))

    if x + helloGameSize[0] > 800:
        x = 800 - helloGameSize[0]
        sound.stop()
        sound.play()

    if y + helloGameSize[1] > 600:
        y = 600 - helloGameSize[1]
        sound.stop()
        sound.play()

    if x<=0:
        x =0
        sound.stop()
        sound.play()
    if y<=0:
        y =0
        sound.stop()
        sound.play()

    screen.blit(helloGame,(x,y))
    pygame.display.update()
