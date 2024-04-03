# import ClientWFunctions as client
# from ClientWFunctions import *
# from soldierTypes import *
import soldierTypes
import StateMachine
import random
import pygame
import socket
import threading
import pickle


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

# which screen to display: s = start menu, c = connection, g = game board, e = end menu, u = user manual/stats
which_screen = "c"

# to stop players from accessing buttons that aren't theirs
player_role = "d"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def send_action(action):
    client.send(pickle.dumps(action))


def handle_server_message():
    global player_role
    while True:
        try:
            message = pickle.loads(client.recv(1024))
            action, data = message

            # if player_role == "g":
            if action == 'create_mortal':
                troop_type = data
                mortal_troop_creation(troop_type)
                print("hi")

            elif action == 'deploy_mortal':
                lane = data
                mortal_troop_deploy(lane)
                print("hi2")

            # if player_role == "m":
            if action == 'create_god':
                troop_type = data
                god_troop_creation(troop_type)
                print("hi3")

            elif action == 'deploy_god':
                lane = data
                god_troop_deploy(lane)
                print("hi4")
            elif action == 'heal_mortal':
                mortal_heal_ability()
            elif action == 'heal_god':
                god_heal_ability()

            if player_role == "d":
                if action == 'choose_god' or action == 'choose_mortal':
                    role = data
                    player_role = role

            pygame.display.update()

        except:
            print("An error occurred!")
            break


def connect_to_server(server_host):
    server_port = 55555

    client.connect((server_host, server_port))

    receive_thread = threading.Thread(target=handle_server_message)
    receive_thread.start()


def crash(mortal, god):
    # if the fighters are in the same lane
    if pygame.sprite.collide_rect(mortal, god):
        fight(mortal, god)
        mortal.crash = True
        god.crash = True


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
        print(str(StateMachine.elapsed_time))
        add_attack_delay(fighter1)

    if can_attack(fighter2):
        print("2")
        fighter1.health -= fighter2.attack_strength
        print(str(fighter1.health))
        print(str(StateMachine.elapsed_time))
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
        if isinstance(fighter, soldierTypes.Archer):
            if fighter.rect.y == StateMachine.lane1_top + StateMachine.top_lane.h - fighter.height:
                archer_in_lane[0] = False
            elif fighter.rect.y == StateMachine.lane2_top + StateMachine.middle_lane.h - fighter.height/2:
                archer_in_lane[1] = False
            elif fighter.rect.y == StateMachine.lane3_top + StateMachine.bottom_lane.h - fighter.height/2:
                archer_in_lane[2] = False
    else:
        god_list.remove(fighter)

        if isinstance(fighter, soldierTypes.Sorceress):
            if fighter.rect.y == StateMachine.lane1_top + StateMachine.top_lane.h - fighter.height/2:
                sorceress_in_lane[0] = False
            elif fighter.rect.y == StateMachine.lane2_top + StateMachine.middle_lane.h - fighter.height/2:
                sorceress_in_lane[1] = False
            elif fighter.rect.y == StateMachine.lane3_top + StateMachine.bottom_lane.h - fighter.height/2:
                sorceress_in_lane[2] = False


def mortal_troop_creation(troop_type):
    global m_tb_pressed

    # create mortal troops to prep for deployment
    if troop_type == 1:
        new_mortal = soldierTypes.FootSoldier()
    elif troop_type == 2:
        new_mortal = soldierTypes.Eagle()
    elif troop_type == 3:
        new_mortal = soldierTypes.Archer()
    elif troop_type == 4:
        new_mortal = soldierTypes.Cavalry()
    elif troop_type == 5:
        new_mortal = soldierTypes.TrojanHorse()
    elif troop_type == 6:
        new_mortal = soldierTypes.Achilles()
    else:
        new_mortal = soldierTypes.FootSoldier()
        # impossible, but just to get the IDE to stop complaining

    # make sure they have enough coins to purchase the troop
    if StateMachine.mortals_coins >= new_mortal.cost:
        mortal_creation_list.append(new_mortal)
        # send_action(('mortal_creation', troop_type))
        # if there is a successful creation, allow for deployment
        m_tb_pressed = True
    else:
        m_tb_pressed = False


def god_troop_creation(troop_type):
    global g_tb_pressed

    # create god troops to prep for deployment
    if troop_type == 1:
        new_god = soldierTypes.Minion()
    elif troop_type == 2:
        new_god = soldierTypes.Harpy()
    elif troop_type == 3:
        new_god = soldierTypes.Sorceress()
    elif troop_type == 4:
        new_god = soldierTypes.Hellhound()
    elif troop_type == 5:
        new_god = soldierTypes.Cyclops()
    elif troop_type == 6:
        new_god = soldierTypes.Medusa()
    else:
        new_god = soldierTypes.Minion()
        # impossible, but just to get the IDE to stop complaining

    if StateMachine.gods_coins >= new_god.cost:
        god_creation_list.append(new_god)
        # send_action(('god_creation', troop_type))
        # if there is a successful creation, allow for deployment
        g_tb_pressed = True
    else:
        g_tb_pressed = False


def buy_mortal(new_mortal):
    mortal_list.add(new_mortal)
    StateMachine.mortals_coins -= new_mortal.cost
    new_mortal.spawn_time = pygame.time.get_ticks()


def buy_god(new_god):
    god_list.add(new_god)
    StateMachine.gods_coins -= new_god.cost
    new_god.spawn_time = pygame.time.get_ticks()


def mortal_troop_deploy(lane):
    global m_tb_pressed

    # If a troop hasn't been chosen (and created when there are enough coins), nothing will happen
    if m_tb_pressed:

        # make the mortal drawable and draw it in the correct lane
        current_mortal = mortal_creation_list[-1]
        current_mortal.rect.x = StateMachine.left_barrier_coord

        if lane == 1:
            current_mortal.rect.y = StateMachine.lane1_top + StateMachine.top_lane.h - current_mortal.height
            if not isinstance(current_mortal, soldierTypes.Archer):
                buy_mortal(current_mortal)
                # send_action(('mortal_deploy', lane))
            else:
                if not archer_in_lane[0]:
                    archer_in_lane[0] = True
                    buy_mortal(current_mortal)
                    # send_action(('mortal_deploy', lane))
                    add_attack_delay(current_mortal)
                else:
                    m_tb_pressed = False
        elif lane == 2:
            current_mortal.rect.y = StateMachine.lane2_top + StateMachine.middle_lane.h - current_mortal.height
            if not isinstance(current_mortal, soldierTypes.Archer):
                buy_mortal(current_mortal)
                # send_action(('mortal_deploy', lane))
            else:
                if not archer_in_lane[1]:
                    archer_in_lane[1] = True
                    buy_mortal(current_mortal)
                    # send_action(('mortal_deploy', lane))
                    add_attack_delay(current_mortal)
                else:
                    m_tb_pressed = False
        elif lane == 3:
            current_mortal.rect.y = StateMachine.lane3_top + StateMachine.bottom_lane.h - current_mortal.height
            if not isinstance(current_mortal, soldierTypes.Archer):
                buy_mortal(current_mortal)
                # send_action(('mortal_deploy', lane))
            else:
                if not archer_in_lane[2]:
                    archer_in_lane[2] = True
                    buy_mortal(current_mortal)
                    # send_action(('mortal_deploy', lane))
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
        current_god.rect.x = StateMachine.right_barrier_coord - current_god.width

        if lane == 1:
            current_god.rect.y = StateMachine.lane1_top + StateMachine.top_lane.h - current_god.height
            if not isinstance(current_god, soldierTypes.Sorceress):
                buy_god(current_god)
                # send_action(('god_deploy', lane))
            else:
                if not sorceress_in_lane[0]:
                    sorceress_in_lane[0] = True
                    buy_god(current_god)
                    # send_action(('god_deploy', lane))
                    add_attack_delay(current_god)
                else:
                    g_tb_pressed = False
        elif lane == 2:
            current_god.rect.y = StateMachine.lane2_top + StateMachine.middle_lane.h - current_god.height
            if not isinstance(current_god, soldierTypes.Sorceress):
                buy_god(current_god)
                # send_action(('god_deploy', lane))
            else:
                if not sorceress_in_lane[1]:
                    sorceress_in_lane[1] = True
                    buy_god(current_god)
                    # send_action(('god_deploy', lane))
                    add_attack_delay(current_god)
                else:
                    g_tb_pressed = False
        elif lane == 3:
            current_god.rect.y = StateMachine.lane3_top + StateMachine.bottom_lane.h - current_god.height
            if not isinstance(current_god, soldierTypes.Sorceress):
                buy_god(current_god)
                # send_action(('god_deploy', lane))
            else:
                if not sorceress_in_lane[2]:
                    sorceress_in_lane[2] = True
                    buy_god(current_god)
                    # send_action(('god_deploy', lane))
                    add_attack_delay(current_god)
                else:
                    g_tb_pressed = False

        # the player has deployed their troop, don't let them do it again
        # (important for coins)
        g_tb_pressed = False


def tower_damage(side, fighter):
    global which_screen

    if fighter.first_hit:
        add_attack_delay(fighter)
        fighter.first_hit = False

    # win/lose condition 2: defeated towers
    if can_attack(fighter):
        add_attack_delay(fighter)

        if side == "r":
            StateMachine.right_tower_health -= fighter.attack_strength
            if StateMachine.right_tower_health <= 0:
                StateMachine.right_tower_health = 0
                StateMachine.draw_game_screen()
                which_screen = "e"
                StateMachine.winner = "Mortals Win!"
        else:
            StateMachine.left_tower_health -= fighter.attack_strength
            if StateMachine.left_tower_health <= 0:
                StateMachine.left_tower_health = 0
                StateMachine.draw_game_screen()
                which_screen = "e"
                StateMachine.winner = "Gods Win!"


def add_attack_delay(fighter):
    delay = random.randint(500, fighter.attack_speed)
    fighter.attack_time_counter = StateMachine.elapsed_time-fighter.spawn_time + delay


def can_attack(fighter):
    # checks that the attack delay has been respected
    return StateMachine.elapsed_time-fighter.spawn_time >= fighter.attack_time_counter


def ranged_hit(fighter, projectile):
    # if fighter collides with arrow/spell
    if pygame.sprite.collide_rect(fighter, projectile) or pygame.sprite.collide_rect(projectile, fighter):
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
    if StateMachine.mortal_coin_level == 1:
        if StateMachine.mortals_coins >= 300:
            StateMachine.mortals_coins -= 300
            StateMachine.mortal_coin_level += 1
    elif StateMachine.mortal_coin_level == 2:
        if StateMachine.mortals_coins >= 500:
            StateMachine.mortals_coins -= 500
            StateMachine.mortal_coin_level += 1


def god_coin_upgrade():
    if StateMachine.god_coin_level == 1:
        if StateMachine.gods_coins >= 300:
            StateMachine.gods_coins -= 300
            StateMachine.god_coin_level += 1
    elif StateMachine.god_coin_level == 2:
        if StateMachine.gods_coins >= 500:
            StateMachine.gods_coins -= 500
            StateMachine.god_coin_level += 1


def mortal_heal_ability():
    if StateMachine.mortals_coins >= 300:
        StateMachine.mortals_coins -= 300
        for mortal in mortal_list:
            mortal.health += int((mortal.max_health - mortal.health) * .5)


def god_heal_ability():
    if StateMachine.gods_coins >= 300:
        StateMachine.gods_coins -= 300
        for god in god_list:
            god.health += int((god.max_health - god.health) * .5)


def start_game():
    global which_screen, m_tb_pressed, g_tb_pressed, archer_in_lane, sorceress_in_lane

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
    StateMachine.right_tower_health = 100
    StateMachine.left_tower_health = 100
    StateMachine.gods_coins = 50
    StateMachine.mortals_coins = 50
    StateMachine.god_coin_level = 1
    StateMachine.mortal_coin_level = 1
    StateMachine.one_second_tracker = 1000
    StateMachine.timed_out = False
    StateMachine.start_time = pygame.time.get_ticks()
