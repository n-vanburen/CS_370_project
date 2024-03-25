import ClientWFunctions
from ClientWFunctions import *
from soldierTypes import *
import StateMachine
import random


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
    if StateMachine.mortals_coins >= new_mortal.cost:
        mortal_creation_list.append(new_mortal)
        # if there is a successful creation, allow for deployment
        ClientWFunctions.m_tb_pressed = True
    else:
        ClientWFunctions.m_tb_pressed = False


def god_troop_creation(troop_type):
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

    if StateMachine.gods_coins >= new_god.cost:
        god_creation_list.append(new_god)
        # if there is a successful creation, allow for deployment
        ClientWFunctions.g_tb_pressed = True
    else:
        ClientWFunctions.g_tb_pressed = False


def buy_mortal(new_mortal):
    mortal_list.add(new_mortal)
    StateMachine.mortals_coins -= new_mortal.cost
    new_mortal.spawn_time = pygame.time.get_ticks()


def buy_god(new_god):
    god_list.add(new_god)
    StateMachine.gods_coins -= new_god.cost
    new_god.spawn_time = pygame.time.get_ticks()


def mortal_troop_deploy(lane):
    # If a troop hasn't been chosen (and created when there are enough coins), nothing will happen
    if ClientWFunctions.m_tb_pressed:

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
                    ClientWFunctions.m_tb_pressed = False
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
                    ClientWFunctions.m_tb_pressed = False
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
                    ClientWFunctions.m_tb_pressed = False

        # the player has deployed their troop, don't let them do it again
        # (important for coins)
        ClientWFunctions.m_tb_pressed = False


def god_troop_deploy(lane):
    # If a troop hasn't been chosen (and created when there are enough coins), nothing will happen
    if ClientWFunctions.g_tb_pressed:

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
                    ClientWFunctions.g_tb_pressed = False
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
                    ClientWFunctions.g_tb_pressed = False
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
                    ClientWFunctions.g_tb_pressed = False

        # the player has deployed their troop, don't let them do it again
        # (important for coins)
        ClientWFunctions.g_tb_pressed = False


def tower_damage(side, fighter):
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
                draw_game_screen()
                ClientWFunctions.which_screen = "e"
                StateMachine.winner = "Mortals Win!"
        else:
            StateMachine.left_tower_health -= fighter.attack_strength
            if StateMachine.left_tower_health <= 0:
                StateMachine.left_tower_health = 0
                draw_game_screen()
                ClientWFunctions.which_screen = "e"
                StateMachine.winner = "Gods Win!"


def add_attack_delay(fighter):
    delay = random.randint(500, fighter.attack_speed)
    fighter.attack_time_counter = StateMachine.elapsed_time-fighter.spawn_time + delay


def can_attack(fighter):
    # checks that the attack delay has been respected
    return StateMachine.elapsed_time-fighter.spawn_time >= fighter.attack_time_counter


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
