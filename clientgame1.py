import pygame
import socket
import threading
import pickle
# import pygame
# import gameBoard
# from gameBoard import *
import gameBoard
from soldierTypes import *
# commented imports are already imported in the soldierTypes file

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_HOST, SERVER_PORT))

def send_action(action):
    client.send(pickle.dumps(action))

pygame.init()

# Your game code here...

# Inside your event loop where troop creation and deployment occur:
# Example event handling:
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click corresponds to troop creation or deployment
            # Example:
            if event.button == 1:  # Left mouse button clicked
                position = event.pos
                action = ("create_troop", position)  # Example action format
                send_action(action)
            elif event.button == 3:  # Right mouse button clicked
                position = event.pos
                action = ("deploy_troop", position)  # Example action format
                send_action(action)
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
    global mortal_creation_index

    # If a troop hasn't been chosen (and created when there are enough coins), nothing will happen
    if m_tb_pressed:

        # make the mortal drawable and draw it in the correct lane
        current_mortal = mortal_creation_list[mortal_creation_index]
        mortal_list.add(current_mortal)
        current_mortal.rect.x = left_barrier_coord

        if lane == 1:
            current_mortal.rect.y = lane1_top + current_mortal.height/2
        elif lane == 2:
            current_mortal.rect.y = lane2_top + current_mortal.height/2
        elif lane == 3:
            current_mortal.rect.y = lane3_top + current_mortal.height/2

        # the player has deployed their troop, don't let them do it again
        # (important for when coins are implemented)
        m_tb_pressed = False
        # increment the index so the next troop deployment doesn't affect this one
        mortal_creation_index += 1


def god_troop_deploy(lane):
    global g_tb_pressed
    global god_creation_index

    # If a troop hasn't been chosen (and created when there are enough coins), nothing will happen
    if g_tb_pressed:

        # make the god drawable and draw it in the correct lane
        current_god = god_creation_list[god_creation_index]
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
        # increment the index so the next troop deployment doesn't affect this one
        god_creation_index += 1


mortal_list = pygame.sprite.Group()
god_list = pygame.sprite.Group()

m_tb_pressed = False
g_tb_pressed = False

mortal_creation_list = []
god_creation_list = []
mortal_creation_index = 0
god_creation_index = 0

running = True
mouse = pygame.mouse.get_pos()
clock = pygame.time.Clock()
while running:
    clock.tick(20)

    screen.fill((0, 0, 0))
    draw_game_screen()

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

# Game over
game_over_text = font.render("Time's up! Game Over!", True, BLACK)
game_over_rect = game_over_text.get_rect(center=(1200 // 2, 700 // 2))
screen.blit(game_over_text, game_over_rect)
pygame.display.flip()

# Wait for a few seconds before quitting
pygame.time.wait(3000)
pygame.quit()
sys.exit()