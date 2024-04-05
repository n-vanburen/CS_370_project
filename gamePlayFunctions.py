# import ClientWFunctions as client
# from ClientWFunctions import *
from soldierTypes import *
import soldierTypes
import StateMachine
import random
import pygame
import socket
import threading
import pickle


random.seed(370)


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

# Music Booleans Initializing ADD MUSIC
game_music = False
connection_music = False
start_music = False
user_manual_stats_music = False

# Music Booleans Initializing Sound Effects
pygame.init()
deploy_footsoldier = pygame.mixer.Sound("deploy_footsoldier.wav")
deploy_eagle = pygame.mixer.Sound("deploy_eagle.wav")
deploy_archer = pygame.mixer.Sound("deploy_archer.wav")
deploy_cavalry = pygame.mixer.Sound("deploy_cavalry.wav")
deploy_trojanhorse = pygame.mixer.Sound("deploy_trojanhorse.wav")
deploy_achilles = pygame.mixer.Sound("deploy_achilles.wav")

deploy_minion = pygame.mixer.Sound("deploy_minion.wav")
deploy_harpy = pygame.mixer.Sound("deploy_harpy.wav")
deploy_sorceress = pygame.mixer.Sound("deploy_sorceress.wav")
deploy_hellhound = pygame.mixer.Sound("deploy_hellhound.wav")
deploy_cyclops = pygame.mixer.Sound("deploy_cyclops.wav")
deploy_medusa = pygame.mixer.Sound("deploy_medusa.wav")

# which screen to display: s = start menu, c = connection, g = game board, e = end menu, u = user manual/stats
which_screen = "c"

# to stop players from accessing buttons that aren't theirs
player_role = "d"

# stats
troops_defeated = 0
troops_spawned = 0
coins_spent = 0
wins = 0
total_td = 0
total_ts = 0
total_cs = 0
# opponent stats
opp_troops_defeated = 0
opp_troops_spawned = 0
opp_coins_spent = 0
opp_wins = 0
total_opp_td = 0
total_opp_ts = 0
total_opp_cs = 0


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def send_action(action):
    client.send(pickle.dumps(action))


def handle_server_message():
    global player_role, opp_troops_spawned, opp_troops_defeated, opp_wins, opp_coins_spent

    while True:
        try:
            message = pickle.loads(client.recv(1024))
            action, data = message

            # if player_role == "g":
            if action == 'create_mortal':
                troop_type = data
                mortal_troop_creation(troop_type)
                print("hi")

            if action == 'deploy_mortal':
                lane = data
                mortal_troop_deploy(lane)
                print("hi2")

            # if player_role == "m":
            if action == 'create_god':
                troop_type = data
                god_troop_creation(troop_type)
                print("hi3")

            if action == 'deploy_god':
                lane = data
                god_troop_deploy(lane)
                print("hi4")

            if action == 'heal_mortal':
                mortal_heal_ability()

            if action == 'heal_god':
                god_heal_ability()

            if player_role == "d":
                if action == 'choose_god' or action == 'choose_mortal':
                    role = data
                    player_role = role

            if action == 'start_game':
                start_game()

            if action == 'god_up_coin':
                god_coin_upgrade()

            if action == 'mortal_up_coin':
                mortal_coin_upgrade()

            if player_role == "m":
                if action == "g_td":
                    opp_troops_defeated = data
                if action == "g_ts":
                    opp_troops_spawned = data
                if action == "g_cs":
                    opp_coins_spent = data
                if action == "g_w":
                    opp_wins = data

            if player_role == "g":
                if action == "m_td":
                    opp_troops_defeated = data
                if action == "m_ts":
                    opp_troops_spawned = data
                if action == "m_cs":
                    opp_coins_spent = data
                if action == "m_w":
                    opp_wins = data

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


def play_attack_sound():
    attack = pygame.mixer.Sound("attack.wav")
    attack.play()


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
        fighter2.health -= fighter1.attack_strength
        play_attack_sound()
        add_attack_delay(fighter1)

    if can_attack(fighter2):
        fighter1.health -= fighter2.attack_strength
        play_attack_sound()
        add_attack_delay(fighter2)

    # check if a fighter has been defeated
    if fighter1.health <= 0:
        defeat(fighter1)
        fighter2.first_hit = True
    if fighter2.health <= 0:
        defeat(fighter2)
        fighter1.first_hit = True


def defeat(fighter):
    global troops_defeated

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

        if player_role == "g":
            troops_defeated += 1

    else:
        god_list.remove(fighter)

        if isinstance(fighter, soldierTypes.Sorceress):
            if fighter.rect.y == StateMachine.lane1_top + StateMachine.top_lane.h - fighter.height/2:
                sorceress_in_lane[0] = False
            elif fighter.rect.y == StateMachine.lane2_top + StateMachine.middle_lane.h - fighter.height/2:
                sorceress_in_lane[1] = False
            elif fighter.rect.y == StateMachine.lane3_top + StateMachine.bottom_lane.h - fighter.height/2:
                sorceress_in_lane[2] = False

        if player_role == "m":
            troops_defeated += 1


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
    global troops_spawned, coins_spent

    mortal_list.add(new_mortal)
    StateMachine.mortals_coins -= new_mortal.cost
    new_mortal.spawn_time = pygame.time.get_ticks()

    if player_role == "m":
        troops_spawned += 1
        coins_spent += new_mortal.cost


def buy_god(new_god):
    global troops_spawned, coins_spent

    god_list.add(new_god)
    StateMachine.gods_coins -= new_god.cost
    new_god.spawn_time = pygame.time.get_ticks()

    if player_role == "g":
        troops_spawned += 1
        coins_spent += new_god.cost


def play_deployment_sound(troop):
    if isinstance(troop, FootSoldier):
        deploy_footsoldier.play()
    if isinstance(troop, Eagle):
        deploy_eagle.play()
    if isinstance(troop, Archer):
        deploy_archer.play()
    if isinstance(troop, Cavalry):
        deploy_cavalry.play()
    if isinstance(troop, TrojanHorse):
        deploy_trojanhorse.play()
    if isinstance(troop, Achilles):
        deploy_achilles.play()

    if isinstance(troop, Minion):
        deploy_minion.play()
    if isinstance(troop, Harpy):
        deploy_harpy.play()
    if isinstance(troop, Sorceress):
        deploy_sorceress.play()
    if isinstance(troop, Hellhound):
        deploy_hellhound.play()
    if isinstance(troop, Cyclops):
        deploy_cyclops.play()
    if isinstance(troop, Medusa):
        deploy_medusa.play()


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
                play_deployment_sound(current_mortal)
                # send_action(('mortal_deploy', lane))
            else:
                if not archer_in_lane[0]:
                    archer_in_lane[0] = True
                    buy_mortal(current_mortal)
                    play_deployment_sound(current_mortal)
                    # send_action(('mortal_deploy', lane))
                    add_attack_delay(current_mortal)
                else:
                    m_tb_pressed = False
        elif lane == 2:
            current_mortal.rect.y = StateMachine.lane2_top + StateMachine.middle_lane.h - current_mortal.height
            if not isinstance(current_mortal, soldierTypes.Archer):
                buy_mortal(current_mortal)
                play_deployment_sound(current_mortal)
                # send_action(('mortal_deploy', lane))
            else:
                if not archer_in_lane[1]:
                    archer_in_lane[1] = True
                    buy_mortal(current_mortal)
                    play_deployment_sound(current_mortal)
                    # send_action(('mortal_deploy', lane))
                    add_attack_delay(current_mortal)
                else:
                    m_tb_pressed = False
        elif lane == 3:
            current_mortal.rect.y = StateMachine.lane3_top + StateMachine.bottom_lane.h - current_mortal.height
            if not isinstance(current_mortal, soldierTypes.Archer):
                buy_mortal(current_mortal)
                play_deployment_sound(current_mortal)
                # send_action(('mortal_deploy', lane))
            else:
                if not archer_in_lane[2]:
                    archer_in_lane[2] = True
                    buy_mortal(current_mortal)
                    play_deployment_sound(current_mortal)
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
                play_deployment_sound(current_god)
                # send_action(('god_deploy', lane))
            else:
                if not sorceress_in_lane[0]:
                    sorceress_in_lane[0] = True
                    buy_god(current_god)
                    play_deployment_sound(current_god)
                    # send_action(('god_deploy', lane))
                    add_attack_delay(current_god)
                else:
                    g_tb_pressed = False
        elif lane == 2:
            current_god.rect.y = StateMachine.lane2_top + StateMachine.middle_lane.h - current_god.height
            if not isinstance(current_god, soldierTypes.Sorceress):
                buy_god(current_god)
                play_deployment_sound(current_god)
                # send_action(('god_deploy', lane))
            else:
                if not sorceress_in_lane[1]:
                    sorceress_in_lane[1] = True
                    buy_god(current_god)
                    play_deployment_sound(current_god)
                    # send_action(('god_deploy', lane))
                    add_attack_delay(current_god)
                else:
                    g_tb_pressed = False
        elif lane == 3:
            current_god.rect.y = StateMachine.lane3_top + StateMachine.bottom_lane.h - current_god.height
            if not isinstance(current_god, soldierTypes.Sorceress):
                buy_god(current_god)
                play_deployment_sound(current_god)
                # send_action(('god_deploy', lane))
            else:
                if not sorceress_in_lane[2]:
                    sorceress_in_lane[2] = True
                    buy_god(current_god)
                    play_deployment_sound(current_god)
                    # send_action(('god_deploy', lane))
                    add_attack_delay(current_god)
                else:
                    g_tb_pressed = False

        # the player has deployed their troop, don't let them do it again
        # (important for coins)
        g_tb_pressed = False


def tower_damage(side, fighter):
    global wins

    if fighter.first_hit:
        add_attack_delay(fighter)
        fighter.first_hit = False

    # win/lose condition 2: defeated towers
    if can_attack(fighter):
        add_attack_delay(fighter)

        if side == "r":
            StateMachine.right_tower_health -= fighter.attack_strength
            play_attack_sound()
            if StateMachine.right_tower_health <= 0:
                StateMachine.right_tower_health = 0
                StateMachine.draw_game_screen()
                StateMachine.winner = "Mortals Win!"
                if player_role == "m":
                    wins += 1
                end_game()
        else:
            StateMachine.left_tower_health -= fighter.attack_strength
            play_attack_sound()
            if StateMachine.left_tower_health <= 0:
                StateMachine.left_tower_health = 0
                StateMachine.draw_game_screen()
                StateMachine.winner = "Gods Win!"
                if player_role == "g":
                    wins += 1
                end_game()


def add_attack_delay(fighter):
    delay = random.randint(500, fighter.attack_speed)
    fighter.attack_time_counter = StateMachine.elapsed_time - fighter.spawn_time + delay


def can_attack(fighter):
    # checks that the attack delay has been respected
    return StateMachine.elapsed_time - fighter.spawn_time >= fighter.attack_time_counter


def ranged_hit(fighter, projectile):
    # if fighter collides with arrow/spell
    if pygame.sprite.collide_rect(fighter, projectile) or pygame.sprite.collide_rect(projectile, fighter):
        # only let a projectile deal damage once
        if not projectile.crash:
            projectile.crash = True

            fighter.health -= projectile.attack_strength
            if isinstance(projectile, Arrow):
                attack = pygame.mixer.Sound("attack_archer.wav")
                attack.play()
            if isinstance(projectile, Spell):
                attack = pygame.mixer.Sound("attack_sorceress.wav")
                attack.play()
            if fighter.health <= 0:
                defeat(fighter)

            if projectile.team == 'm':
                arrow_list.remove(projectile)
            else:
                spell_list.remove(projectile)


def mortal_coin_upgrade():
    global coins_spent

    if StateMachine.mortals_coins >= StateMachine.m_upgrade_cost and StateMachine.mortal_coin_level <= 2:
        StateMachine.mortals_coins -= StateMachine.m_upgrade_cost
        StateMachine.mortal_coin_level += 1
        if player_role == "m":
            coins_spent += StateMachine.m_upgrade_cost


def god_coin_upgrade():
    global coins_spent

    if StateMachine.gods_coins >= StateMachine.g_upgrade_cost and StateMachine.god_coin_level <= 2:
        StateMachine.gods_coins -= StateMachine.g_upgrade_cost
        StateMachine.mortal_coin_level += 1
        if player_role == "g":
            coins_spent += StateMachine.g_upgrade_cost


def mortal_heal_ability():
    global coins_spent

    if StateMachine.mortals_coins >= 300:
        StateMachine.mortals_coins -= 300
        for mortal in mortal_list:
            mortal.health += int((mortal.max_health - mortal.health) * .5)
        if player_role == "m":
            coins_spent += 300


def god_heal_ability():
    global coins_spent

    if StateMachine.gods_coins >= 300:
        StateMachine.gods_coins -= 300
        for god in god_list:
            god.health += int((god.max_health - god.health) * .5)
        if player_role == "g":
            coins_spent += 300


def music_unload_and_new(music):
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)


def start_game():
    global which_screen, m_tb_pressed, g_tb_pressed, archer_in_lane, sorceress_in_lane, player_role, troops_spawned
    global troops_defeated, coins_spent

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
    troops_defeated = 0
    troops_spawned = 0
    coins_spent = 0


def end_game():
    global which_screen, total_td, total_cs, total_ts, total_opp_td, total_opp_cs, total_opp_ts

    which_screen = 'e'

    # string that is sent over network depends on player role
    td_action = player_role + "_troops_defeated"
    ts_action = player_role + "_troops_spawned"
    cs_action = player_role + "_coins_spent"
    wins_action = player_role + "_wins"

    # send the stats for the opponent's display
    send_action((td_action, troops_defeated))
    send_action((ts_action, troops_spawned))
    send_action((cs_action, coins_spent))
    send_action((wins_action, wins))

    total_td += troops_defeated
    total_ts += troops_spawned
    total_cs += coins_spent

    total_opp_td += opp_troops_defeated
    total_opp_ts += opp_troops_spawned
    total_opp_cs += opp_coins_spent
