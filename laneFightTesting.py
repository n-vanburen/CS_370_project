# import pygame
# import gameBoard
# from gameBoard import *
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


# other possible functions:
    # Initializing the fighters -- takes number for what button (one for mortal one for god)
    # deploying the fighters -- takes number for what lane (one for mortal one for god)

mortal_list = pygame.sprite.Group()
god_list = pygame.sprite.Group()

m_tb_pressed = False
g_tb_pressed = False

running = True
mouse = pygame.mouse.get_pos()
clock = pygame.time.Clock()
while running:
    clock.tick(20)

    screen.fill((0, 0, 0))
    draw_game_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            # mortal troop choices -- make deployment possible and create the fighters
            if (m_tb_1.left <= mouse[0] <= m_tb_1.left+tb_width
                    and m_tb_1.top <= mouse[1] <= m_tb_1.top+tb_height):
                mortal = FootSoldier()
                m_tb_pressed = True
                # initializes a fighter and makes deployment possible
                print("mortal troop 1 button pressed")
            elif (m_tb_2.left <= mouse[0] <= m_tb_2.left+tb_width
                    and m_tb_2.top <= mouse[1] <= m_tb_2.top+tb_height):
                mortal = Eagle()
                m_tb_pressed = True
                print("mortal troop 2 button pressed")
            elif (m_tb_3.left <= mouse[0] <= m_tb_3.left+tb_width
                    and m_tb_3.top <= mouse[1] <= m_tb_3.top+tb_height):
                mortal = Archer()
                m_tb_pressed = True
                print("mortal troop 3 button pressed")
            elif (m_tb_4.left <= mouse[0] <= m_tb_4.left+tb_width
                    and m_tb_4.top <= mouse[1] <= m_tb_4.top+tb_height):
                mortal = Cavalry()
                m_tb_pressed = True
                print("mortal troop 4 button pressed")
            elif (m_tb_5.left <= mouse[0] <= m_tb_5.left+tb_width
                    and m_tb_5.top <= mouse[1] <= m_tb_5.top+tb_height):
                mortal = TrojanHorse()
                m_tb_pressed = True
                print("mortal troop 5 button pressed")
            elif (m_tb_6.left <= mouse[0] <= m_tb_6.left+tb_width
                    and m_tb_6.top <= mouse[1] <= m_tb_6.top+tb_height):
                mortal = Achilles()
                m_tb_pressed = True
                print("mortal troop 6 button pressed")

            # mortal deployment lane choices -- spawn the fighter created above in correct lane
            elif (m_deploy1.left <= mouse[0] <= m_deploy1.left+t_deploy_width
                    and m_deploy1.top <= mouse[1] <= m_deploy1.top+t_deploy_height):
                if m_tb_pressed:
                    mortal_list.add(mortal)
                    mortal.rect.x = right_barrier_coord - mortal.width
                    mortal.rect.y = lane1_top + mortal.height/2
                    # deploy the mortal to the chosen lane
                    m_tb_pressed = False
                    # reset the pressed_variable so, they can't just spawn another
                    print("Mortal deployment for lane 1 pressed")
            elif (m_deploy2.left <= mouse[0] <= m_deploy2.left+t_deploy_width
                    and m_deploy2.top <= mouse[1] <= m_deploy2.top+t_deploy_height):
                if m_tb_pressed:
                    mortal_list.add(mortal)
                    mortal.rect.x = right_barrier_coord - mortal.width
                    mortal.rect.y = lane2_top + mortal.height/2
                    m_tb_pressed = False
                    print("Mortal deployment for lane 2 pressed")
            elif (m_deploy3.left <= mouse[0] <= m_deploy3.left+t_deploy_width
                  and m_deploy3.top <= mouse[1] <= m_deploy3.top+t_deploy_height):
                if m_tb_pressed:
                    mortal_list.add(mortal)
                    mortal.rect.x = right_barrier_coord - mortal.width
                    mortal.rect.y = lane2_top + mortal.height/2
                    m_tb_pressed = False
                    print("Mortal deployment for lane 3 pressed")
            else:
                m_tb_pressed = False
                # if they didn't choice a valid deployment, nothing will happen

            # god troop choices -- make deployment possible and create the fighters
            if (g_tb_1.left <= mouse[0] <= g_tb_1.left+tb_width
                    and g_tb_1.top <= mouse[1] <= g_tb_1.top+tb_height):
                god = Minion()
                g_tb_pressed = True
                # initializes a fighter and makes deployment possible
            elif (g_tb_2.left <= mouse[0] <= g_tb_2.left+tb_width
                    and g_tb_2.top <= mouse[1] <= g_tb_2.top+tb_height):
                god = Harpy()
                g_tb_pressed = True
            elif (g_tb_3.left <= mouse[0] <= g_tb_3.left+tb_width
                    and g_tb_3.top <= mouse[1] <= g_tb_3.top+tb_height):
                god = Sorceress()
                g_tb_pressed = True
            elif (g_tb_4.left <= mouse[0] <= g_tb_4.left+tb_width
                    and g_tb_4.top <= mouse[1] <= g_tb_4.top+tb_height):
                god = Hellhound()
                g_tb_pressed = True
            elif (g_tb_5.left <= mouse[0] <= g_tb_5.left+tb_width
                    and g_tb_5.top <= mouse[1] <= g_tb_5.top+tb_height):
                god = Cyclops
                g_tb_pressed = True
            elif (g_tb_6.left <= mouse[0] <= g_tb_6.left+tb_width
                    and g_tb_6.top <= mouse[1] <= g_tb_6.top+tb_height):
                god = Medusa()
                g_tb_pressed = True

            # mortal deployment lane choices -- spawn the fighter created above in correct lane
            elif (g_deploy1.left <= mouse[0] <= g_deploy1.left+t_deploy_width
                    and g_deploy1.top <= mouse[1] <= g_deploy1.top+t_deploy_height):
                if g_tb_pressed:
                    god_list.add(god)
                    god.rect.x = right_barrier_coord - god.width
                    god.rect.y = lane1_top + god.height/2
                    # deploy the god to the chosen lane
                    g_tb_pressed = False
                    # reset the pressed_variable so, they can't just spawn another
            elif (g_deploy2.left <= mouse[0] <= g_deploy2.left+t_deploy_width
                  and g_deploy2.top <= mouse[1] <= g_deploy2.top+t_deploy_height):
                if g_tb_pressed:
                    god_list.add(god)
                    god.rect.x = right_barrier_coord - god.width
                    god.rect.y = lane2_top + god.height/2
                    g_tb_pressed = False
            elif (g_deploy3.left <= mouse[0] <= g_deploy3.left+t_deploy_width
                  and g_deploy3.top <= mouse[1] <= g_deploy3.top+t_deploy_height):
                if g_tb_pressed:
                    god_list.add(god)
                    god.rect.x = right_barrier_coord - god.width
                    god.rect.y = lane3_top + god.height/2
                    g_tb_pressed = False
            else:
                g_tb_pressed = False
                # if they didn't choice a valid deployment, nothing will happen

    # get the new mouse position
    mouse = pygame.mouse.get_pos()

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
