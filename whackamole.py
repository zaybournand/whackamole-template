import pygame
import random

# Initialize Pygame and set up the screen
pygame.init()
width, height = 20 * 32, 16 * 32  # Grid of 20x16 squares, each 32x32
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Whack-a-Mole")

# Colors
light_green = (144, 238, 144)
black = (0, 0, 0)

# Load the mole image
mole_image = pygame.image.load("mole.png")  # Replace with the correct path to mole.png
mole_rect = mole_image.get_rect(topleft=(0, 0))  # Start mole in the top-left square

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mole was clicked
            if mole_rect.collidepoint(event.pos):
                # Move the mole to a random position in the grid
                mole_rect.topleft = (random.randint(0, 19) * 32, random.randint(0, 15) * 32)

    # Fill the screen with a light green background color
    screen.fill(light_green)

    # Draw the grid lines
    for x in range(0, width, 32):
        pygame.draw.line(screen, black, (x, 0), (x, height))
    for y in range(0, height, 32):
        pygame.draw.line(screen, black, (0, y), (width, y))

    # Draw the mole
    screen.blit(mole_image, mole_rect)

    # Update the display
    pygame.display.flip()

pygame.quit()
