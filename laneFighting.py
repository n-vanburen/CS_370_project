import sys
import random
import gameBoard
from soldierTypes import *
from StartMenu import *
import StartMenu
import os


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

    # ensure the first attack is not simultaneous
    if fighter1.first_hit:
        add_attack_delay(fighter1)
        fighter1.first_hit = False
    if fighter2.first_hit:
        add_attack_delay(fighter2)
        fighter2.first_hit = False

    # deal damage while having collided (attack delay applicable)
    if can_attack(fighter1):
        print("1")
        fighter2.health -= fighter1.attack_strength
        print(str(fighter2.health))
        print(str(gameBoard.elapsed_time))
        add_attack_delay(fighter1)

    if can_attack(fighter2):
        print("2")
        fighter1.health -= fighter2.attack_strength
        print(str(fighter1.health))
        print(str(gameBoard.elapsed_time))
        add_attack_delay(fighter2)

    # check if a fighter has been defeated
    if fighter1.health <= 0:
        defeat(fighter1)
        fighter2.first_hit = True
    if fighter2.health <= 0:
        defeat(fighter2)
        fighter1.first_hit = True


def defeat(fighter):
    if fighter.team == 'm':
        mortal_list.remove(fighter)

        # for the handling of a single archer per lane
        if isinstance(fighter, Archer):
            if fighter.rect.y == lane1_top + fighter.height/2:
                archer_in_lane[0] = False
            elif fighter.rect.y == lane2_top + fighter.height/2:
                archer_in_lane[1] = False
            elif fighter.rect.y == lane3_top + fighter.height/2:
                archer_in_lane[2] = False
    else:
        god_list.remove(fighter)

        if isinstance(fighter, Sorceress):
            if fighter.rect.y == lane1_top + fighter.height/2:
                sorceress_in_lane[0] = False
            elif fighter.rect.y == lane2_top + fighter.height/2:
                sorceress_in_lane[1] = False
            elif fighter.rect.y == lane3_top + fighter.height/2:
                sorceress_in_lane[2] = False


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

    # make sure they have enough coins to purchase the troop
    if gameBoard.mortals_coins >= new_mortal.cost:
        mortal_creation_list.append(new_mortal)
        # if there is a successful creation, allow for deployment
        m_tb_pressed = True
    else:
        m_tb_pressed = False


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

    if gameBoard.gods_coins >= new_god.cost:
        god_creation_list.append(new_god)
        # if there is a successful creation, allow for deployment
        g_tb_pressed = True
    else:
        g_tb_pressed = False


def buy_mortal(new_mortal):
    mortal_list.add(new_mortal)
    gameBoard.mortals_coins -= new_mortal.cost
    new_mortal.spawn_time = pygame.time.get_ticks()


def buy_god(new_god):
    god_list.add(new_god)
    gameBoard.gods_coins -= new_god.cost
    new_god.spawn_time = pygame.time.get_ticks()


def mortal_troop_deploy(lane):
    global m_tb_pressed

    # If a troop hasn't been chosen (and created when there are enough coins), nothing will happen
    if m_tb_pressed:

        # make the mortal drawable and draw it in the correct lane
        current_mortal = mortal_creation_list[-1]
        current_mortal.rect.x = left_barrier_coord

        if lane == 1:
            current_mortal.rect.y = lane1_top + current_mortal.height/2
            if not isinstance(current_mortal, Archer):
                buy_mortal(current_mortal)
            else:
                if not archer_in_lane[0]:
                    archer_in_lane[0] = True
                    buy_mortal(current_mortal)
                    add_attack_delay(current_mortal)
                else:
                    m_tb_pressed = False
        elif lane == 2:
            current_mortal.rect.y = lane2_top + current_mortal.height/2
            if not isinstance(current_mortal, Archer):
                buy_mortal(current_mortal)
            else:
                if not archer_in_lane[1]:
                    archer_in_lane[1] = True
                    buy_mortal(current_mortal)
                    add_attack_delay(current_mortal)
                else:
                    m_tb_pressed = False
        elif lane == 3:
            current_mortal.rect.y = lane3_top + current_mortal.height/2
            if not isinstance(current_mortal, Archer):
                buy_mortal(current_mortal)
            else:
                if not archer_in_lane[2]:
                    archer_in_lane[2] = True
                    buy_mortal(current_mortal)
                    add_attack_delay(current_mortal)
                else:
                    m_tb_pressed = False

        # the player has deployed their troop, don't let them do it again
        # (important for coins)
        m_tb_pressed = False


def god_troop_deploy(lane):
    global g_tb_pressed

    # If a troop hasn't been chosen (and created when there are enough coins), nothing will happen
    if g_tb_pressed:

        # make the god drawable and draw it in the correct lane
        current_god = god_creation_list[-1]
        current_god.rect.x = right_barrier_coord - current_god.width

        if lane == 1:
            current_god.rect.y = lane1_top + current_god.height/2
            if not isinstance(current_god, Sorceress):
                buy_god(current_god)
            else:
                if not sorceress_in_lane[0]:
                    sorceress_in_lane[0] = True
                    buy_god(current_god)
                    add_attack_delay(current_god)
                else:
                    g_tb_pressed = False
        elif lane == 2:
            current_god.rect.y = lane2_top + current_god.height/2
            if not isinstance(current_god, Sorceress):
                buy_god(current_god)
            else:
                if not sorceress_in_lane[1]:
                    sorceress_in_lane[1] = True
                    buy_god(current_god)
                    add_attack_delay(current_god)
                else:
                    g_tb_pressed = False
        elif lane == 3:
            current_god.rect.y = lane3_top + current_god.height/2
            if not isinstance(current_god, Sorceress):
                buy_god(current_god)
            else:
                if not sorceress_in_lane[2]:
                    sorceress_in_lane[2] = True
                    buy_god(current_god)
                    add_attack_delay(current_god)
                else:
                    g_tb_pressed = False

        # the player has deployed their troop, don't let them do it again
        # (important for coins)
        g_tb_pressed = False


def mortal_heal_ability():
    for mortal in mortal_list:
        mortal.health += 50
        #if mortal.health > mortal.max_health:
            #mortal.health = mortal.max_health
        mortal.update_health_label()
        mortal.update()



def tower_damage(side, fighter):
    global running
    global which_screen

    if fighter.first_hit:
        add_attack_delay(fighter)
        fighter.first_hit = False

    # win/lose condition 2: defeated towers
    if can_attack(fighter):
        add_attack_delay(fighter)

        if side == "r":
            gameBoard.right_tower_health -= fighter.attack_strength
            if gameBoard.right_tower_health <= 0:
                gameBoard.right_tower_health = 0
                draw_game_screen()
                which_screen = "e"
                StartMenu.winner = "Mortals Win!"
        else:
            gameBoard.left_tower_health -= fighter.attack_strength
            if gameBoard.left_tower_health <= 0:
                gameBoard.left_tower_health = 0
                draw_game_screen()
                which_screen = "e"
                StartMenu.winner = "Gods Win!"


def add_attack_delay(fighter):
    delay = random.randint(500, fighter.attack_speed)
    fighter.attack_time_counter = gameBoard.elapsed_time-fighter.spawn_time + delay


def can_attack(fighter):
    # checks that the attack delay has been respected
    return gameBoard.elapsed_time-fighter.spawn_time >= fighter.attack_time_counter


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


def mortal_coin_upgrade():
    if gameBoard.mortal_coin_level == 1:
        if gameBoard.mortals_coins >= 300:
            gameBoard.mortals_coins -= 300
            gameBoard.mortal_coin_level += 1
    elif gameBoard.mortal_coin_level == 2:
        if gameBoard.mortals_coins >= 500:
            gameBoard.mortals_coins -= 500
            gameBoard.mortal_coin_level += 1


def god_coin_upgrade():
    if gameBoard.god_coin_level == 1:
        if gameBoard.gods_coins >= 300:
            gameBoard.gods_coins -= 300
            gameBoard.god_coin_level += 1
    elif gameBoard.god_coin_level == 2:
        if gameBoard.gods_coins >= 500:
            gameBoard.gods_coins -= 500
            gameBoard.god_coin_level += 1


# which screen to display: s = start menu, c = connection, g = gameBoard, e = end menu, u = user manual/stats
which_screen = "c"

# get the ip of the localhost
ip = os.popen('ipconfig').read()
index = ip.find("IPv4", ip.find("IPv4")+1)
# localhost_ip = ip[index+36:index+50]
localhost_ip = ip[index+36: ip.find(" ", index+36)-1]

mortal_list = pygame.sprite.Group()
god_list = pygame.sprite.Group()

arrow_list = pygame.sprite.Group()
spell_list = pygame.sprite.Group()

m_tb_pressed = False
g_tb_pressed = False
mortal_creation_list = []
god_creation_list = []

archer_in_lane = [False, False, False]
sorceress_in_lane = [False, False, False]

# font = pygame.font.SysFont("Font.tff", 36)

running = True
clock = pygame.time.Clock()
while running:
    clock.tick(20)

    if which_screen == "g":
        screen.fill((0, 0, 0))
        draw_game_screen()

        # win/lose condition 1: time ran out
        if gameBoard.timed_out:
            which_screen = "e"
            StartMenu.winner = "Time's Up! No Winner!"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                # mortal troop choices -- make deployment possible and create the fighters
                if m_tb_1.collidepoint(event.pos):
                    mortal_troop_creation(1)
                elif m_tb_2.collidepoint(event.pos):
                    mortal_troop_creation(2)
                elif m_tb_3.collidepoint(event.pos):
                    mortal_troop_creation(3)
                elif m_tb_4.collidepoint(event.pos):
                    mortal_troop_creation(4)
                elif m_tb_5.collidepoint(event.pos):
                    mortal_troop_creation(5)
                elif m_tb_6.collidepoint(event.pos):
                    mortal_troop_creation(6)

                # mortal deployment lane choices -- spawn the fighter created above in correct lane
                elif m_deploy1.collidepoint(event.pos):
                    mortal_troop_deploy(1)
                elif m_deploy2.collidepoint(event.pos):
                    mortal_troop_deploy(2)
                elif m_deploy3.collidepoint(event.pos):
                    mortal_troop_deploy(3)
                else:
                    m_tb_pressed = False
                    # if they didn't choice a valid deployment, nothing will happen

                # god troop choices -- make deployment possible and create the fighters
                if g_tb_1.collidepoint(event.pos):
                    god_troop_creation(1)
                elif g_tb_2.collidepoint(event.pos):
                    god_troop_creation(2)
                elif g_tb_3.collidepoint(event.pos):
                    god_troop_creation(3)
                elif g_tb_4.collidepoint(event.pos):
                    god_troop_creation(4)
                elif g_tb_5.collidepoint(event.pos):
                    god_troop_creation(5)
                elif g_tb_6.collidepoint(event.pos):
                    god_troop_creation(6)

                # mortal deployment lane choices -- spawn the fighter created above in correct lane
                elif g_deploy1.collidepoint(event.pos):
                    god_troop_deploy(1)
                elif g_deploy2.collidepoint(event.pos):
                    god_troop_deploy(2)
                elif g_deploy3.collidepoint(event.pos):
                    god_troop_deploy(3)
                else:
                    g_tb_pressed = False
                    # if they didn't choose a valid deployment, nothing will happen

                # Coin Upgrade Test Mortal/God
                if m_coin_upgrade_b.collidepoint(event.pos):
                    mortal_coin_upgrade()
                if g_coin_upgrade_b.collidepoint(event.pos):
                    god_coin_upgrade()

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
                if can_attack(mortal):
                    new_arrow = Arrow()
                    arrow_list.add(new_arrow)
                    new_arrow.rect.x = mortal.rect.x + mortal.width
                    new_arrow.rect.y = mortal.rect.y + mortal.height/2 - new_arrow.height/2

                    random_attack_delay = random.randint(mortal.attack_speed/2, mortal.attack_speed)
                    mortal.attack_time_counter = gameBoard.elapsed_time-mortal.spawn_time + random_attack_delay

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
                if can_attack(god):
                    new_spell = Spell()
                    spell_list.add(new_spell)
                    new_spell.rect.x = god.rect.x - new_spell.width
                    new_spell.rect.y = god.rect.y + god.height/2 - new_spell.height/2

                    random_attack_delay = random.randint(god.attack_speed/2, god.attack_speed)
                    god.attack_time_counter = gameBoard.elapsed_time-god.spawn_time + random_attack_delay

        # move the arrows/spells and de-spawn them if they're out of range
        for arrow in arrow_list:
            arrow.move_right(arrow.speed)
            if arrow.halfway:
                arrow_list.remove(arrow)
        for spell in spell_list:
            spell.move_left(spell.speed)
            if spell.halfway:
                spell_list.remove(spell)

        # draw sprites
        mortal_list.draw(screen)
        god_list.draw(screen)
        arrow_list.draw(screen)
        spell_list.draw(screen)

        # update health labels (after .draw() so that it isn't overwritten)
        for mortal in mortal_list:
            mortal.update_health_label()
            mortal.update()
        for god in god_list:
            god.update_health_label()
            god.update()

    elif which_screen == "s":
        StartMenu.draw_start_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                # start the game
                if start_b.collidepoint(event.pos):
                    # check that both players have clicked start before starting (NEEDED)
                    which_screen = "g"
                    # reset all variables, so it's a new game in case this is round 2
                    mortal_list.empty()
                    god_list.empty()
                    arrow_list.empty()
                    spell_list.empty()
                    m_tb_pressed = False
                    g_tb_pressed = False
                    mortal_creation_list.clear()
                    god_creation_list.clear()
                    archer_in_lane = [False, False, False]
                    sorceress_in_lane = [False, False, False]
                    gameBoard.right_tower_health = 100
                    gameBoard.left_tower_health = 100
                    gameBoard.gods_coins = 50
                    gameBoard.mortals_coins = 50
                    gameBoard.god_coin_level = 1
                    gameBoard.mortal_coin_level = 1
                    gameBoard.one_second_tracker = 1000
                    gameBoard.timed_out = False
                    gameBoard.start_time = pygame.time.get_ticks()
                # display stats
                if stats_b.collidepoint(event.pos):
                    which_screen = "u"
                # quit game
                if quit_b.collidepoint(event.pos):
                    running = False

    elif which_screen == "c":
        StartMenu.draw_connection_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    StartMenu.ip_displayed = ""
                    StartMenu.input_box_active = True
                else:
                    StartMenu.input_box_active = False

                if get_ip_b.collidepoint(event.pos):
                    StartMenu.ip_displayed = localhost_ip
                if connect_b.collidepoint(event.pos):
                    which_screen = "s"
                    # for now (NEEDS TO CHANGE), just go to start menu (until networking added here)
                    # Connect to the server with whatever ip_displayed is (NEEDED)

                # both clients have connected (boolean list in server) (one will have clicked host server)
                # and at least one chose a role (choice blacked out for other player)
                # both connect and a role have to have been clicked
                # then, the start menu will be displayed (NEEDED)

            # This is how the input box text is changed by the user
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if StartMenu.input_box_active:
                        # store current text minus last char
                        StartMenu.ip_displayed = StartMenu.ip_displayed[:-1]
                else:
                    if StartMenu.input_box_active:
                        StartMenu.ip_displayed += event.unicode

    elif which_screen == "u":
        draw_stats_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_b.collidepoint(event.pos):
                    which_screen = "s"

    elif which_screen == "e":
        draw_end_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_b.collidepoint(event.pos):
                    which_screen = "s"
                elif new_opp_b.collidepoint(event.pos):
                    which_screen = "c"
                elif e_quit_b.collidepoint(event.pos):
                    running = False

    pygame.display.update()

# Game over (temporary until a game-over screen)
"""if gameBoard.timed_out:
    game_over_text = main_font.render("Time's up! Game Over!", True, BLACK)
elif right_tower_defeat:
    game_over_text = main_font.render("Game Over! Mortals Win!", True, BLACK)
elif left_tower_defeat:
    game_over_text = main_font.render("Game Over! Gods Win!", True, BLACK)
else:
    game_over_text = main_font.render("", True, BLACK)
    # this one will only happen if a player closes the window prematurely

game_over_rect = game_over_text.get_rect(center=(1200 // 2, 700 // 2))
screen.blit(game_over_text, game_over_rect)"""
pygame.display.flip()

# Wait for a few seconds before quitting
# pygame.time.wait(3000)
pygame.quit()
sys.exit()
