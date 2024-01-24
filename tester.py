
import pygame

pygame.init()

# CREATING CANVAS
canvas = pygame.display.set_mode((800, 500))

WHITE = (255, 255, 255)
# LEFT TOWER
tower1 = pygame.Rect(30, 200, 70, 70)
pygame.draw.rect(canvas, WHITE, tower1, 2)
# RIGHT TOWER
tower2 = pygame.Rect(700, 200, 70, 70)
pygame.draw.rect(canvas, WHITE, tower2, 2)
# LEFT BARRIER LINE
pygame.draw.line(canvas, WHITE, (150,0), (150,500), 1)
# RIGHT BARRIER LINE
pygame.draw.line(canvas, WHITE, (650,0), (650,500), 1)



# TITLE OF CANVAS
pygame.display.set_caption("My Board")
exit = False

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.display.update()


