# tutorial: https://www.geeksforgeeks.org/python-drawing-design-using-arrow-keys-in-pygame/?ref=lbp
import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Arrow Drawings')

# marker current coordinates
x = 200
y = 200

# dimensions of marker
width = 10
height = 10

# speed of movement
velocity = 5

running = True
while running:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_LEFT] and x > 0:
        x -= velocity

    if keys_pressed[pygame.K_RIGHT] and x < 500:
        x += velocity

    if keys_pressed[pygame.K_UP] and y > 0:
        y -= velocity

    if keys_pressed[pygame.K_DOWN] and y < 500:
        y += velocity

    # drawing spot on screen (rectangle here)
    pygame.draw.rect(screen, (255, 0, 0), [x, y, width, height])

    pygame.display.update()

pygame.quit()
