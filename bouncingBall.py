# tutorial: https://www.geeksforgeeks.org/adding-boundary-to-an-object-in-pygame/?ref=lbp
import pygame
import random
pygame.init()

width = 700
height = 550

blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode((width, height))

# ball variables
ball_X = width/2-12
ball_Y = height/2-12
ball_XChange = 1 * random.choice((1, -1))
ball_YChange = 1
ballPixel = 12

# smaller boundary - rectangle variables
rect_left = width/4
rect_top = height/4
rect_width = width/2
rect_height = height/2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if ball_X+ballPixel >= rect_width+rect_left or ball_X-ballPixel <= rect_left:
        ball_XChange *= -1
    if ball_Y+ballPixel >= rect_height+rect_top or ball_Y-ballPixel <= rect_top:
        ball_YChange *= -1

    ball_X += ball_XChange
    ball_Y += ball_YChange

    pygame.time.delay(10)

    screen.fill(black)

    ball = pygame.draw.circle(screen, blue, (ball_X, ball_Y), 12)
    boundary_rect = pygame.draw.rect(screen, white, [rect_left, rect_top, rect_width, rect_height], 2)

    pygame.display.update()

pygame.quit()