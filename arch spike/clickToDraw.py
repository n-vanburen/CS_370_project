# from tutorial: https://www.geeksforgeeks.org/pygame-drawing-objects-and-shapes/?ref=lbp

import pygame
pygame.init()

window = pygame.display.set_mode((600, 600))
window.fill((255, 255, 255))

circle_pos = []
circle_radius = 60
color = (0, 0, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # stores a new coordinate where you will draw a circle based on where you click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = event.pos
            circle_pos.append(position)

    # draws the circles where you've clicked
    for position in circle_pos:
        pygame.draw.circle(window, color, position, circle_radius)

    pygame.display.update()
