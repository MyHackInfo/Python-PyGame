import pygame
pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
# Display Window Title
pygame.display.set_caption("Slither")

pygame.display.update()
gameExit = False
while not gameExit:
    # Here is all Event of pgame 
    for event in pygame.event.get():
        print(event)


pygame.quit()
quit()
