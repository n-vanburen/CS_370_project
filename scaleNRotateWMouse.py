# tutorial: https://www.geeksforgeeks.org/how-to-use-the-mouse-to-scale-and-rotate-an-image-in-pygame/?ref=lbp

import pygame
import math
# so you don't have to type pygame.eventType later
from pygame.locals import *
pygame.init()

color_1 = (82, 122, 86)
color_2 = (53.7, 81.2, 94.1)
color_3 = (255, 170, 51)

screen_size = (w, h) = (600, 600)
screen = pygame.display.set_mode(screen_size)

img = pygame.image.load("Tower.png")
img.convert()

rect = img.get_rect()
pygame.draw.rect(img, color_1, rect, 1)
center = w//2, h//2
rect.center = center

mouse = pygame.mouse.get_pos()

running = True
angle = 0
scale = 1

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:

            # what is K_ra and K_sa??????
            if event.key == K_ra:

                # mod is all modifier keys in a pressed state, bitwise & lets us check for specific ones
                if event.mod & KMOD_SHIFT:

                    # angle at which it should move left
                    angle -= 1
                else:

                    # angle at which it should move right
                    angle += 1
            elif event.key == K_sa:
                if event.mod & KMOD_SHIFT:
                    scale /= 1
                else:
                    scale *= 1

        elif event.type == MOUSEMOTION:
            mouse = event.pos
            x = mouse[0] - center[0]
            y = mouse[1] - center[1]
            # distance between the 2 points (0,0 and (x,y)
            d = math.sqrt(x ** 2 + y ** 2)
            # atan2() returns arctangent of y/x in radians
            angle = math.degrees(-math.atan2(y, x))
            scale = abs(5 * d / w)
            img = pygame.transform.rotozoom(img, angle, scale)
            rect = img.get_rect()
            rect.center = center

    screen.fill(color_3)
    screen.blit(img, rect)

    # rectangle, line, and circles to help in moving the image
    pygame.draw.rect(screen, color_2, rect, 3)
    pygame.draw.line(screen, color_3, center, mouse, 2)
    pygame.draw.circle(screen, color_1, center, 5, 1)
    pygame.draw.circle(screen, color_2, mouse, 5, 1)

    pygame.display.update()

pygame.quit()
