import pygame
import random


pygame.init()
width, height = 20 * 32, 16 * 32  
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Whack-a-Mole")


light_green = (144, 238, 144)
black = (0, 0, 0)


mole_image = pygame.image.load("mole.png")
mole_rect = mole_image.get_rect(topleft=(0, 0))  


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            if mole_rect.collidepoint(event.pos):
               
                mole_rect.topleft = (random.randint(0, 19) * 32, random.randint(0, 15) * 32)

    
    screen.fill(light_green)

    
    for x in range(0, width, 32):
        pygame.draw.line(screen, black, (x, 0), (x, height))
    for y in range(0, height, 32):
        pygame.draw.line(screen, black, (0, y), (width, y))

    
    screen.blit(mole_image, mole_rect)

    pygame.display.flip()

pygame.quit()
