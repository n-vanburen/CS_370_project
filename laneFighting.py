import sys
import gameBoard
from soldierTypes import *


def crash(fighter1, fighter2):
    # if the fighters are in the same lane
    if fighter1.rect.y == fighter2.rect.y:
        # if fighter1 collides with fighter2
        if (fighter1.rect.x <= fighter2.rect.x <= fighter1.rect.x+fighter1.width
                or fighter1.rect.x <= fighter2.rect.x+fighter2.width <= fighter1.rect.x+fighter1.width):
            fight(fighter1, fighter2)
            fighter1.crash = True
            fighter2.crash = True


def fight(fighter1, fighter2):
    # stop moving
    fighter1.moving = False
    fighter2.moving = False

    # deal damage while having collided
    fighter1.health -= fighter2.attack_strength
    fighter2.health -= fighter1.attack_strength

    # check if a fighter has been defeated
    if fighter1.health <= 0:
        defeat(fighter1)
    if fighter2.health <= 0:
        defeat(fighter2)


def defeat(fighter):
    if fighter.team == 'm':
        mortal_list.remove(fighter)

        # for the handling of a single archer per lane
        if isinstance(fighter, Archer):
            if fighter.rect.y
    else:
        god_list.remove(fighter)


def mortal_troop_creation(troop_type):
    global m_tb_pressed

    # create mortal troops to prep for deployment
    if troop_type == 1:
        new_mortal = FootSoldier()
    elif troop_type == 2:
        new_mortal = Eagle()
    elif troop_type == 3:
        new_mortal = Archer()
    elif troop_type == 4:
        new_mortal = Cavalry()
    elif troop_type == 5:
        new_mortal = TrojanHorse()
    elif troop_type == 6:
        new_mortal = Achilles()
    else:
        new_mortal = FootSoldier()
        # impossible, but just to get the IDE to stop complaining

    mortal_creation_list.append(new_mortal)

    # if there is a successful creation, allow for deployment
    m_tb_pressed = True


def god_troop_creation(troop_type):
    global g_tb_pressed

    # create god troops to prep for deployment
    if troop_type == 1:
        new_god = Minion()
    elif troop_type == 2:
        new_god = Harpy()
    elif troop_type == 3:
        new_god = Sorceress()
    elif troop_type == 4:
        new_god = Hellhound()
    elif troop_type == 5:
        new_god = Cyclops()
    elif troop_type == 6:
        new_god = Medusa()
    else:
        new_god = Minion()
        # impossible, but just to get the IDE to stop complaining

    god_creation_list.append(new_god)

    # if there is a successful creation, allow for deployment
    g_tb_pressed = True


def mortal_troop_deploy(lane):
    global m_tb_pressed

    # If a troop hasn't been chosen (and created when there are enough coins), nothing will happen
    if m_tb_pressed:

        # make the mortal drawable and draw it in the correct lane
        current_mortal = mortal_creation_list[-1]
        current_mortal.rect.x = left_barrier_coord

        if lane == 1:
            current_mortal.rect.y = lane1_top + current_mortal.height/2
            if isinstance(current_mortal, Archer):
                if not archer_in_lane[0]:
                    archer_in_lane[0] = True
                    mortal_list.add(current_mortal)
                else:
                    m_tb_pressed = False
            else:
                mortal_list.add(current_mortal)
        elif lane == 2:
            current_mortal.rect.y = lane2_top + current_mortal.height/2
            if isinstance(current_mortal, Archer):
                if not archer_in_lane[1]:
                    archer_in_lane[1] = True
                    mortal_list.add(current_mortal)
                else:
                    m_tb_pressed = False
            else:
                mortal_list.add(current_mortal)
        elif lane == 3:
            current_mortal.rect.y = lane3_top + current_mortal.height/2
            if isinstance(current_mortal, Archer):
                if not archer_in_lane[2]:
                    archer_in_lane[2] = True
                    mortal_list.add(current_mortal)
                else:
                    m_tb_pressed = False
            else:
                mortal_list.add(current_mortal)

        # the player has deployed their troop, don't let them do it again
        # (important for when coins are implemented)
        m_tb_pressed = False


def god_troop_deploy(lane):
    global g_tb_pressed

    # If a troop hasn't been chosen (and created when there are enough coins), nothing will happen
    if g_tb_pressed:

        # make the god drawable and draw it in the correct lane
        current_god = god_creation_list[-1]
        god_list.add(current_god)
        current_god.rect.x = right_barrier_coord - current_god.width

        if lane == 1:
            current_god.rect.y = lane1_top + current_god.height/2
        elif lane == 2:
            current_god.rect.y = lane2_top + current_god.height/2
        elif lane == 3:
            current_god.rect.y = lane3_top + current_god.height/2

        # the player has deployed their troop, don't let them do it again
        # (important for when coins are implemented)
        g_tb_pressed = False


def tower_damage(side, fighter):
    global running
    global left_tower_defeat
    global right_tower_defeat

    # win/lose condition 2: defeated towers

    if side == "r":
        gameBoard.right_tower_health -= fighter.attack_strength
        if gameBoard.right_tower_health <= 0:
            gameBoard.right_tower_health = 0
            right_tower_defeat = True
            draw_game_screen()
            running = False
    else:
        gameBoard.left_tower_health -= fighter.attack_strength
        if gameBoard.left_tower_health <= 0:
            gameBoard.left_tower_health = 0
            left_tower_defeat = True
            draw_game_screen()
            running = False


def ranged_hit(fighter, projectile):
    # if they are in the same lane
    if (fighter.rect.y <= projectile.rect.y <= fighter.rect.y+fighter.height
            or fighter.rect.y <= projectile.rect.y+projectile.height <= fighter.rect.y+fighter.height):
        # if fighter collides with arrow/spell
        if (fighter.rect.x <= projectile.rect.x <= fighter.rect.x+fighter.width
                or fighter.rect.x <= projectile.rect.x+projectile.width <= fighter.rect.x+fighter.width):
            # only let a projectile deal damage once
            if not projectile.crash:
                projectile.crash = True

                fighter.health -= projectile.attack_strength
                if fighter.health <= 0:
                    defeat(fighter)

                if projectile.team == 'm':
                    arrow_list.remove(projectile)
                else:
                    spell_list.remove(projectile)


mortal_list = pygame.sprite.Group()
god_list = pygame.sprite.Group()

arrow_list = pygame.sprite.Group()
spell_list = pygame.sprite.Group()

m_tb_pressed = False
g_tb_pressed = False
mortal_creation_list = []
god_creation_list = []

right_tower_defeat = False
left_tower_defeat = False

archer_in_lane = [False, False, False]
sorceress_in_lane = [False, False, False]

font = pygame.font.SysFont("Font.tff", 36)

running = True
mouse = pygame.mouse.get_pos()
clock = pygame.time.Clock()
while running:
    clock.tick(20)

    screen.fill((0, 0, 0))
    draw_game_screen()

    # win/lose condition 1: time ran out
    if gameBoard.timed_out:
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            # mortal troop choices -- make deployment possible and create the fighters
            if (m_tb_1.left <= mouse[0] <= m_tb_1.left+tb_width
                    and m_tb_1.top <= mouse[1] <= m_tb_1.top+tb_height):
                mortal_troop_creation(1)
            elif (m_tb_2.left <= mouse[0] <= m_tb_2.left+tb_width
                    and m_tb_2.top <= mouse[1] <= m_tb_2.top+tb_height):
                mortal_troop_creation(2)
            elif (m_tb_3.left <= mouse[0] <= m_tb_3.left+tb_width
                    and m_tb_3.top <= mouse[1] <= m_tb_3.top+tb_height):
                mortal_troop_creation(3)
            elif (m_tb_4.left <= mouse[0] <= m_tb_4.left+tb_width
                    and m_tb_4.top <= mouse[1] <= m_tb_4.top+tb_height):
                mortal_troop_creation(4)
            elif (m_tb_5.left <= mouse[0] <= m_tb_5.left+tb_width
                    and m_tb_5.top <= mouse[1] <= m_tb_5.top+tb_height):
                mortal_troop_creation(5)
            elif (m_tb_6.left <= mouse[0] <= m_tb_6.left+tb_width
                    and m_tb_6.top <= mouse[1] <= m_tb_6.top+tb_height):
                mortal_troop_creation(6)

            # mortal deployment lane choices -- spawn the fighter created above in correct lane
            elif (m_deploy1.left <= mouse[0] <= m_deploy1.left+t_deploy_width
                    and m_deploy1.top <= mouse[1] <= m_deploy1.top+t_deploy_height):
                mortal_troop_deploy(1)
            elif (m_deploy2.left <= mouse[0] <= m_deploy2.left+t_deploy_width
                    and m_deploy2.top <= mouse[1] <= m_deploy2.top+t_deploy_height):
                mortal_troop_deploy(2)
            elif (m_deploy3.left <= mouse[0] <= m_deploy3.left+t_deploy_width
                  and m_deploy3.top <= mouse[1] <= m_deploy3.top+t_deploy_height):
                mortal_troop_deploy(3)
            else:
                m_tb_pressed = False
                # if they didn't choice a valid deployment, nothing will happen

            # god troop choices -- make deployment possible and create the fighters
            if (g_tb_1.left <= mouse[0] <= g_tb_1.left+tb_width
                    and g_tb_1.top <= mouse[1] <= g_tb_1.top+tb_height):
                god_troop_creation(1)
            elif (g_tb_2.left <= mouse[0] <= g_tb_2.left+tb_width
                    and g_tb_2.top <= mouse[1] <= g_tb_2.top+tb_height):
                god_troop_creation(2)
            elif (g_tb_3.left <= mouse[0] <= g_tb_3.left+tb_width
                    and g_tb_3.top <= mouse[1] <= g_tb_3.top+tb_height):
                god_troop_creation(3)
            elif (g_tb_4.left <= mouse[0] <= g_tb_4.left+tb_width
                    and g_tb_4.top <= mouse[1] <= g_tb_4.top+tb_height):
                god_troop_creation(4)
            elif (g_tb_5.left <= mouse[0] <= g_tb_5.left+tb_width
                    and g_tb_5.top <= mouse[1] <= g_tb_5.top+tb_height):
                god_troop_creation(5)
            elif (g_tb_6.left <= mouse[0] <= g_tb_6.left+tb_width
                    and g_tb_6.top <= mouse[1] <= g_tb_6.top+tb_height):
                god_troop_creation(6)

            # mortal deployment lane choices -- spawn the fighter created above in correct lane
            elif (g_deploy1.left <= mouse[0] <= g_deploy1.left+t_deploy_width
                    and g_deploy1.top <= mouse[1] <= g_deploy1.top+t_deploy_height):
                god_troop_deploy(1)
            elif (g_deploy2.left <= mouse[0] <= g_deploy2.left+t_deploy_width
                  and g_deploy2.top <= mouse[1] <= g_deploy2.top+t_deploy_height):
                god_troop_deploy(2)
            elif (g_deploy3.left <= mouse[0] <= g_deploy3.left+t_deploy_width
                  and g_deploy3.top <= mouse[1] <= g_deploy3.top+t_deploy_height):
                god_troop_deploy(3)
            else:
                g_tb_pressed = False
                # if they didn't choose a valid deployment, nothing will happen

    # get the new mouse position
    mouse = pygame.mouse.get_pos()

    # long-ranged attacks
    # check to see if anyone got hit by an arrow/spell
    for mortal in mortal_list:
        for spell in spell_list:
            ranged_hit(mortal, spell)
    for god in god_list:
        for arrow in arrow_list:
            ranged_hit(god, arrow)

    # short range attacks
    # see if any monster in the lane is colliding
    for mortal in mortal_list:
        for god in god_list:
            crash(mortal, god)

    # move the players
    for mortal in mortal_list:
        if mortal.moving:
            mortal.move_right(mortal.speed)

        # if they've reached the tower already, but a troop is spawned to push them back
        if mortal.crash and mortal.hit_right_barrier:
            mortal.rect.x -= mortal.width
            mortal.hit_right_barrier = False
        # otherwise, they can attack the tower
        elif mortal.hit_right_barrier:
            tower_damage("r", mortal)

        # reset crash and moving in case of defeat for next run
        mortal.crash = False
        mortal.moving = True

        # if the mortal is an archer, launch an arrow (delay based on elapsed time later)
        if isinstance(mortal, Archer):
            if gameBoard.elapsed_time % 10000 <= 50:
                new_arrow = Arrow()
                arrow_list.add(new_arrow)
                new_arrow.rect.x = mortal.rect.x + mortal.width
                new_arrow.rect.y = mortal.rect.y + mortal.height/2 - new_arrow.height/2

    for god in god_list:
        if god.moving:
            god.move_left(god.speed)

        if god.crash and god.hit_left_barrier:
            god.rect.x -= god.width
            god.hit_left_barrier = False
        elif god.hit_left_barrier:
            tower_damage("l", god)

        god.crash = False
        god.moving = True

        if isinstance(god, Sorceress):
            if gameBoard.elapsed_time % 5000 <= 50:
                new_spell = Spell()
                spell_list.add(new_spell)
                new_spell.rect.x = god.rect.x - new_spell.width
                new_spell.rect.y = god.rect.y + god.height/2 - new_spell.height/2

    for arrow in arrow_list:
        arrow.move_right(arrow.speed)
        if arrow.halfway:
            arrow_list.remove(arrow)
    for spell in spell_list:
        spell.move_left(spell.speed)
        if spell.halfway:
            spell_list.remove(spell)

    # updates
    mortal_list.draw(screen)
    god_list.draw(screen)
    arrow_list.draw(screen)
    spell_list.draw(screen)

    # update health label (after .draw() so that it isn't overwritten
    for mortal in mortal_list:
        mortal.update_health_label()
        mortal.update()
    for god in god_list:
        god.update_health_label()
        god.update()

    pygame.display.update()

# Game over
if gameBoard.timed_out:
    game_over_text = font.render("Time's up! Game Over!", True, BLACK)
elif right_tower_defeat:
    game_over_text = font.render("Game Over! Mortals Win!", True, BLACK)
elif left_tower_defeat:
    game_over_text = font.render("Game Over! Gods Win!", True, BLACK)
else:
    game_over_text = font.render("", True, BLACK)
    # impossible but to get IDE to stop complaining

game_over_rect = game_over_text.get_rect(center=(1200 // 2, 700 // 2))
screen.blit(game_over_text, game_over_rect)
pygame.display.flip()

# Wait for a few seconds before quitting
pygame.time.wait(3000)
pygame.quit()
sys.exit()
