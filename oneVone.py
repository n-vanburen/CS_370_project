from soldierTypes import *
# pygame is already imported in the soldierTypes file


def crash(fighter1, fighter2):
    # if fighter1 collides with fighter2 horizontally
    if (fighter1.rect.x <= fighter2.rect.x <= fighter1.rect.x+fighter1.width
            or fighter1.rect.x <= fighter2.rect.x+fighter2.width <= fighter1.rect.x+fighter1.width):
        fight(fighter1, fighter2)


def fight(fighter1, fighter2):
    # stop moving
    fighter1.moving = False
    fighter2.moving = False

    # deal damage while having collided
    fighter1.health -= fighter2.attack_strength
    fighter2.health -= fighter1.attack_strength
    print(str(fighter1.health))
    print(str(fighter2.health))

    # check if a fighter has been defeated
    if fighter1.health <= 0:
        defeat(fighter1)
        fighter2.moving = True
    if fighter2.health <= 0:
        defeat(fighter2)
        fighter1.moving = True


def defeat(fighter):
    print('defeat')
    if fighter.team == 'm':
        mortal_list.remove(fighter)
    else:
        god_list.remove(fighter)


screen = pygame.display.set_mode((800, 500))

player = TrojanHorse()
player.rect.x = 0
player.rect.y = 200

enemy = Hellhound()
enemy.rect.x = 750
enemy.rect.y = 200

enemy2 = Hellhound()
enemy2.rect.x = 900
enemy2.rect.y = 200

mortal_list = pygame.sprite.Group()
god_list = pygame.sprite.Group()

mortal_list.add(player)
god_list.add(enemy)
god_list.add(enemy2)

running = True
clock = pygame.time.Clock()
while running:
    clock.tick(20)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # see if any monster in the lane is colliding
    for mortal in mortal_list:
        for god in god_list:
            crash(mortal, god)

    # move the players
    for mortal in mortal_list:
        if mortal.moving:
            mortal.move_right(mortal.speed)
    for god in god_list:
        if god.moving:
            god.move_left(god.speed)

    # updates
    mortal_list.update()
    god_list.update()
    mortal_list.draw(screen)
    god_list.draw(screen)

    # update health label (after .draw() so that it isn't overwritten
    for mortal in mortal_list:
        mortal.update_health_label()
    for god in god_list:
        god.update_health_label()

    pygame.display.update()

pygame.quit()
