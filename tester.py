import pygame

pygame.init()

# CREATING CANVAS/SIZE - Week 2
canvas = pygame.display.set_mode((1200, 700))
# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (150, 150, 150)
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
timer = pygame.draw.rect(canvas, BLACK, pygame.Rect(500, 0, 200, 75),2)
# Mortal Ability Buttons - Week 3
mortal_ability1 = pygame.draw.rect(canvas, BLACK, pygame.Rect(0, 0, 105, 105), 2)
mortal_ability2 = pygame.draw.rect(canvas, BLACK, pygame.Rect(105, 0, 105, 105), 2)
mortal_coins = pygame.draw.rect(canvas, BLACK, pygame.Rect(10, 520, 80, 40), 2)
mortal_upgrades = pygame.draw.rect(canvas, BLACK, pygame.Rect(120, 520, 80, 40), 2)
mortal_troop1 = pygame.draw.rect(canvas, BLACK, pygame.Rect(0, 565, 70, 70), 2)
mortal_troop2 = pygame.draw.rect(canvas, BLACK, pygame.Rect(70, 565, 70, 70), 2)
mortal_troop3 = pygame.draw.rect(canvas, BLACK, pygame.Rect(140, 565, 70, 70), 2)
mortal_troop4 = pygame.draw.rect(canvas, BLACK, pygame.Rect(0, 635, 70, 70), 2)
mortal_troop5 = pygame.draw.rect(canvas, BLACK, pygame.Rect(70, 635, 70, 70), 2)
mortal_troop6 = pygame.draw.rect(canvas, BLACK, pygame.Rect(140, 635, 70, 70), 2)
# God Ability Buttons - Week 3
god_ability1 = pygame.draw.rect(canvas, BLACK, pygame.Rect(990, 0, 105, 105), 2)
god_ability2 = pygame.draw.rect(canvas, BLACK, pygame.Rect(1095, 0, 105, 105), 2)
god_coins = pygame.draw.rect(canvas, BLACK, pygame.Rect(1000, 520, 80, 40), 2)
god_upgrades = pygame.draw.rect(canvas, BLACK, pygame.Rect(1110, 520, 80, 40), 2)
god_troop1 = pygame.draw.rect(canvas, BLACK, pygame.Rect(990, 565, 70, 70), 2)
god_troop2 = pygame.draw.rect(canvas, BLACK, pygame.Rect(1060, 565, 70, 70), 2)
god_troop3 = pygame.draw.rect(canvas, BLACK, pygame.Rect(1130, 565, 70, 70), 2)
god_troop4 = pygame.draw.rect(canvas, BLACK, pygame.Rect(990, 635, 70, 70), 2)
god_troop5 = pygame.draw.rect(canvas, BLACK, pygame.Rect(1060, 635, 70, 70), 2)
god_troop6 = pygame.draw.rect(canvas, BLACK, pygame.Rect(1130, 635, 70, 70), 2)
# LANES - Week 4
top_lane = pygame.draw.rect(canvas, BLACK, pygame.Rect(210, 175, 782, 100), 2)
middle_lane = pygame.draw.rect(canvas, BLACK, pygame.Rect(210, 275, 782, 100), 2)
bottom_lane = pygame.draw.rect(canvas, BLACK, pygame.Rect(210, 375, 782, 100), 2)
# Human Troop Deploy Zones - Week 4
human_deploy1 = pygame.draw.rect(canvas, GREY, pygame.Rect(170, 176, 40, 98), 0)
human_deploy2 = pygame.draw.rect(canvas, GREY, pygame.Rect(170, 276, 40, 98), 0)
human_deploy3 = pygame.draw.rect(canvas, GREY, pygame.Rect(170, 376, 40, 98), 0)
# God Troop Deploy Zones - Week 4
god_deploy1 = pygame.draw.rect(canvas, GREY, pygame.Rect(992, 176, 40, 98), 0)
god_deploy2 = pygame.draw.rect(canvas, GREY, pygame.Rect(992, 276, 40, 98), 0)
god_deploy3 = pygame.draw.rect(canvas, GREY, pygame.Rect(992, 376, 40, 98), 0)


# TITLE OF CANVAS
pygame.display.set_caption("My Board")
exit = False

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.display.update()
