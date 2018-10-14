import pygame
import time
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Hunter")

clock = pygame.time.Clock()

block_size = 10
FPS = 30

font = pygame.font.SysFont(None,40)

def message_to_screen(msg,color):
    screen_text = font.render(msg,True,color)
    gameDisplay.blit(screen_text, [display_width/2,display_height/2])

# Here first crete gameLoop function
# Store some variable that can be use for this function
def gameLoop():
    # Like this variable
    gameExit = False
    # Here create gameOver variable
    gameOver = False
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0

    while not gameExit:
        # Here create while loop for msg C or Q.
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit",red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change - 0

        if lead_x >=display_width or lead_x < 0 or lead_y >=display_height or lead_y < 0:
            # Here change gameExit to gameOver
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(red)
        pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,block_size,block_size])
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

gameLoop()
