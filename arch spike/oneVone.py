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


# screen = pygame.display.set_mode((800, 500))

player = TrojanHorse()
player.rect.x = 0
player.rect.y = 200

player2 = Achilles()
player2.rect.x = -150
player2.rect.y = 200

player3 = FootSoldier()
player3.rect.x = -300
player3.rect.y = 200

player4 = Eagle()
player4.rect.x = -450
player4.rect.y = 200

player5 = Archer()
player5.rect.x = 0
player5.rect.y = 200

player6 = Cavalry()
player6.rect.x = -600
player6.rect.y = 200

enemy = Hellhound()
enemy.rect.x = 750
enemy.rect.y = 200

enemy2 = Minion()
enemy2.rect.x = 900
enemy2.rect.y = 200

enemy3 = Medusa()
enemy3.rect.x = 1050
enemy3.rect.y = 200

enemy4 = Harpy()
enemy4.rect.x = 1200
enemy4.rect.y = 200

enemy5 = Cyclops()
enemy5.rect.x = 1350
enemy5.rect.y = 200

enemy6 = Sorceress()
enemy6.rect.x = screen.get_width()-enemy6.width
enemy6.rect.y = 200

mortal_list = pygame.sprite.Group()
god_list = pygame.sprite.Group()

mortal_list.add(player)
mortal_list.add(player2)
mortal_list.add(player3)
mortal_list.add(player4)
mortal_list.add(player5)
mortal_list.add(player6)
god_list.add(enemy)
god_list.add(enemy2)
god_list.add(enemy3)
god_list.add(enemy4)
god_list.add(enemy5)
god_list.add(enemy6)

running = True
clock = pygame.time.Clock()
while running:
    clock.tick(20)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # what troop
            # get lane
            # create troop
            # spawn(lane, troop)

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
    mortal_list.draw(screen)
    god_list.draw(screen)

    # update health label (after .draw() so that it isn't overwritten
    for mortal in mortal_list:
        mortal.update_health_label()
        mortal.update()
    for god in god_list:
        god.update_health_label()
        god.update()

    pygame.display.update()

pygame.quit()
