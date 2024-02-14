# from tutorial: https://www.geeksforgeeks.org/how-to-move-an-image-with-the-mouse-in-pygame/?ref=lbp

import pygame
pygame.init()

color_1 = (173, 216, 230)
color_2 = (200, 162, 200)

size = (w, h) = (600, 600)
screen = pygame.display.set_mode(size)

img = pygame.image.load('Tower.png')
# makes pixel format of the image the same as the display surface (best for blit)
img.convert()

print('Image size: ' + str(img.get_size()))

# optional for more attractive output: rectangle border
rect = img.get_rect()
# // is floor division
rect.center = w//2, h//2

running = True
moving = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse click was on the rectangle surrounding the image
            if rect.collidepoint(event.pos):
                moving = True
        elif event.type == pygame.MOUSEBUTTONUP:
            moving = False

        elif event.type == pygame.MOUSEMOTION and moving:
            rect.move_ip(event.rel)

    screen.fill(color_1)
    screen.blit(img, rect)

    # optional border to image
    pygame.draw.rect(screen, color_2, rect, 2)

    pygame.display.update()

pygame.quit()
