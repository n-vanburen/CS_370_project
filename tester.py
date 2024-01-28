import pygame

pygame.init()

# CREATING CANVAS/SIZE
canvas = pygame.display.set_mode((1200, 700))
# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
# BACKGROUND
background = pygame.image.load('Background.png').convert()
backgroundTransform = pygame.transform.scale(background, (1200, 700))
canvas.blit(backgroundTransform, (0, 0))
pygame.display.update()
# LEFT TOWER
tower1 = pygame.image.load('Tower.png').convert()
towerTransform1 = pygame.transform.scale(tower1, (100, 100))
canvas.blit(towerTransform1, (50, 300))
pygame.display.update()
towerRectangle1 = pygame.Rect(50, 300, 100, 100)
pygame.draw.rect(canvas, BLACK, towerRectangle1, 2)
# RIGHT TOWER
tower2 = pygame.image.load('Tower.png').convert()
towerTransform2 = pygame.transform.scale(tower2, (100, 100))
canvas.blit(towerTransform2, (1050, 300))
pygame.display.update()
towerRectangle2 = pygame.Rect(1050, 300, 100, 100)
pygame.draw.rect(canvas, BLACK, towerRectangle2, 2)
# LEFT BARRIER LINE
pygame.draw.line(canvas, BLACK, (200, 0), (200, 700), 2)
# RIGHT BARRIER LINE
pygame.draw.line(canvas, BLACK, (1000, 0), (1000, 700), 2)

# TITLE OF CANVAS
pygame.display.set_caption("My Board")
exit = False

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.display.update()
