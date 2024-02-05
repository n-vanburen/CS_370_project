import pygame

pygame.init()

# CREATING CANVAS/SIZE - Week 2
canvas = pygame.display.set_mode((1200, 700))
# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
# BACKGROUND - Week 2
background = pygame.image.load('Background.png').convert()
backgroundTransform = pygame.transform.scale(background, (1200, 700))
canvas.blit(backgroundTransform, (0, 0))
pygame.display.update()
# LEFT TOWER - Week 2
tower1 = pygame.image.load('Tower.png').convert()
towerTransform1 = pygame.transform.scale(tower1, (100, 100))
canvas.blit(towerTransform1, (25, 275))
pygame.display.update()
towerRectangle1 = pygame.Rect(25, 275, 100, 100)
pygame.draw.rect(canvas, BLACK, towerRectangle1, 2)
# RIGHT TOWER - Week 2
tower2 = pygame.image.load('Tower.png').convert()
towerTransform2 = pygame.transform.scale(tower2, (100, 100))
canvas.blit(towerTransform2, (1075, 275))
pygame.display.update()
towerRectangle2 = pygame.Rect(1075, 275, 100, 100)
pygame.draw.rect(canvas, BLACK, towerRectangle2, 2)
# LEFT BARRIER LINE - Week 2
pygame.draw.line(canvas, BLACK, (210, 0), (210, 700), 2)
# RIGHT BARRIER LINE
pygame.draw.line(canvas, BLACK, (990, 0), (990, 700), 2)
# Center Top Timer Box - Week 3
timer = pygame.Rect(500, 0, 200, 75)
pygame.draw.rect(canvas, BLACK, timer, 2)
# Mortal Ability Buttons - Week 3
mortal_ability1 = pygame.Rect(0, 0, 105, 105)
pygame.draw.rect(canvas, BLACK, mortal_ability1, 2)
mortal_ability2 = pygame.Rect(105, 0, 105, 105)
pygame.draw.rect(canvas, BLACK, mortal_ability2, 2)
mortal_coins = pygame.Rect(10, 520, 80, 40)
pygame.draw.rect(canvas, BLACK, mortal_coins, 2)
mortal_upgrades = pygame.Rect(120, 520, 80, 40)
pygame.draw.rect(canvas, BLACK, mortal_upgrades, 2)
mortal_troop1 = pygame.Rect(0, 565, 70, 70)
pygame.draw.rect(canvas, BLACK, mortal_troop1, 2)
mortal_troop2 = pygame.Rect(70, 565, 70, 70)
pygame.draw.rect(canvas, BLACK, mortal_troop2, 2)
mortal_troop3 = pygame.Rect(140, 565, 70, 70)
pygame.draw.rect(canvas, BLACK, mortal_troop3, 2)
mortal_troop4 = pygame.Rect(0, 635, 70, 70)
pygame.draw.rect(canvas, BLACK, mortal_troop4, 2)
mortal_troop5 = pygame.Rect(70, 635, 70, 70)
pygame.draw.rect(canvas, BLACK, mortal_troop5, 2)
mortal_troop6 = pygame.Rect(140, 635, 70, 70)
pygame.draw.rect(canvas, BLACK, mortal_troop6, 2)
# God Ability Buttons - Week 3
god_ability1 = pygame.Rect(990, 0, 105, 105)
pygame.draw.rect(canvas, BLACK, god_ability1, 2)
god_ability2 = pygame.Rect(1095, 0, 105, 105)
pygame.draw.rect(canvas, BLACK, god_ability2, 2)
god_coins = pygame.Rect(1000, 520, 80, 40)
pygame.draw.rect(canvas, BLACK, god_coins, 2)
god_upgrades = pygame.Rect(1110, 520, 80, 40)
pygame.draw.rect(canvas, BLACK, god_upgrades, 2)
god_troop1 = pygame.Rect(990, 565, 70, 70)
pygame.draw.rect(canvas, BLACK, god_troop1, 2)
god_troop2 = pygame.Rect(1060, 565, 70, 70)
pygame.draw.rect(canvas, BLACK, god_troop2, 2)
god_troop3 = pygame.Rect(1130, 565, 70, 70)
pygame.draw.rect(canvas, BLACK, god_troop3, 2)
god_troop4 = pygame.Rect(990, 635, 70, 70)
pygame.draw.rect(canvas, BLACK, god_troop4, 2)
god_troop5 = pygame.Rect(1060, 635, 70, 70)
pygame.draw.rect(canvas, BLACK, god_troop5, 2)
god_troop6 = pygame.Rect(1130, 635, 70, 70)
pygame.draw.rect(canvas, BLACK, god_troop6, 2)
# LANES - Week 4
top_lane = pygame.Rect(210, 175, 782, 100)
pygame.draw.rect(canvas, BLACK, top_lane, 2)
middle_lane = pygame.Rect(210, 275, 782, 100)
pygame.draw.rect(canvas, BLACK, middle_lane, 2)
bottom_lane = pygame.Rect(210, 375, 782, 100)
pygame.draw.rect(canvas, BLACK, bottom_lane, 2)


# TITLE OF CANVAS
pygame.display.set_caption("My Board")
exit = False

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.display.update()
