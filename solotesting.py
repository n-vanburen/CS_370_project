import gamePlayFunctions
from gamePlayFunctions import *
from soldierTypes import *
import StateMachine
from StateMachine import *
import sys
import os
import random

random.seed(370)

# get the ip of the localhost
ip = os.popen('ipconfig').read()
index = ip.find("IPv4", ip.find("IPv4")+1)
# localhost_ip = ip[index+36:index+50]
localhost_ip = ip[index+36: ip.find(" ", index+36)-1]

# font = pygame.font.SysFont("Font.tff", 36)

running = True
clock = pygame.time.Clock()
while running:
    clock.tick(20)

    if gamePlayFunctions.which_screen == "g":
        screen.fill((0, 0, 0))
        draw_game_screen()
        if not gamePlayFunctions.game_music:
            gamePlayFunctions.game_music = True
            music_unload_and_new("Music3.wav")

        # win/lose condition 1: time ran out
        if StateMachine.timed_out:
            if StateMachine.right_tower_health > StateMachine.left_tower_health:
                StateMachine.winner = "Times up! Mortals Win!"
                if gamePlayFunctions.player_role == "m":
                    gamePlayFunctions.wins += 1
            elif StateMachine.left_tower_health > StateMachine.right_tower_health:
                StateMachine.winner = "Times up! Gods Win!"
                if gamePlayFunctions.player_role == "g":
                    gamePlayFunctions.wins += 1
            else:
                StateMachine.winner = "Time's Up! No Winner!"
            end_game()
            send_action((player_role + "_troops_defeated", troops_defeated))
            send_action((player_role + "_troops_spawned", troops_spawned))
            send_action((player_role + "_coins_spent", coins_spent))
            send_action((player_role + "_wins", wins))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                # mortal's buttons
                if gamePlayFunctions.player_role == "m":
                    # mortal troop choices -- make deployment possible and create the fighters
                    if m_tb_1.collidepoint(event.pos):
                        # gamePlayFunctions.mortal_troop_creation(1)
                        send_action(('mortal_creation', 1))
                    elif m_tb_2.collidepoint(event.pos):
                        # gamePlayFunctions.mortal_troop_creation(2)
                        send_action(('mortal_creation', 2))
                    elif m_tb_3.collidepoint(event.pos):
                        # gamePlayFunctions.mortal_troop_creation(3)
                        send_action(('mortal_creation', 3))
                    elif m_tb_4.collidepoint(event.pos):
                        # gamePlayFunctions.mortal_troop_creation(4)
                        send_action(('mortal_creation', 4))
                    elif m_tb_5.collidepoint(event.pos):
                        # gamePlayFunctions.mortal_troop_creation(5)
                        send_action(('mortal_creation', 5))
                    elif m_tb_6.collidepoint(event.pos):
                        # gamePlayFunctions.mortal_troop_creation(6)
                        send_action(('mortal_creation', 6))

                    # mortal deployment lane choices -- spawn the fighter created above in correct lane
                    elif m_deploy1.collidepoint(event.pos):
                        # gamePlayFunctions.mortal_troop_deploy(1)
                        send_action(('mortal_deploy', 1))
                    elif m_deploy2.collidepoint(event.pos):
                        # gamePlayFunctions.mortal_troop_deploy(2)
                        send_action(('mortal_deploy', 2))
                    elif m_deploy3.collidepoint(event.pos):
                        # gamePlayFunctions.mortal_troop_deploy(3)
                        send_action(('mortal_deploy', 3))
                    else:
                        m_tb_pressed = False
                        # if they didn't choice a valid deployment, nothing will happen

                    # Coin Upgrade Test
                    if m_coin_upgrade_b.collidepoint(event.pos):
                        gamePlayFunctions.mortal_coin_upgrade()
                        send_action(('coin_up_mortal', 'holder'))
                    if m_ability2_b.collidepoint(event.pos):
                        # mortal_heal_ability()
                        send_action(('mortal_heal', "holder"))

                    if m_ability1_b.collidepoint(event.pos):
                        gamePlayFunctions.catapult_pressed = True
                    elif ((top_lane.collidepoint(event.pos) or middle_lane.collidepoint(event.pos) or
                           bottom_lane.collidepoint(event.pos))):
                        if gamePlayFunctions.catapult_pressed:
                            catapult_attack(event.pos)
                    else:
                        gamePlayFunctions.catapult_pressed = False

                # gods' buttons
                else:
                    # god troop choices -- make deployment possible and create the fighters
                    if g_tb_1.collidepoint(event.pos):
                        # gamePlayFunctions.god_troop_creation(1)
                        send_action(('god_creation', 1))
                    elif g_tb_2.collidepoint(event.pos):
                        # gamePlayFunctions.god_troop_creation(2)
                        send_action(('god_creation', 2))
                    elif g_tb_3.collidepoint(event.pos):
                        # gamePlayFunctions.god_troop_creation(3)
                        send_action(('god_creation', 3))
                    elif g_tb_4.collidepoint(event.pos):
                        # gamePlayFunctions.god_troop_creation(4)
                        send_action(('god_creation', 4))
                    elif g_tb_5.collidepoint(event.pos):
                        # gamePlayFunctions.god_troop_creation(5)
                        send_action(('god_creation', 5))
                    elif g_tb_6.collidepoint(event.pos):
                        # gamePlayFunctions.god_troop_creation(6)
                        send_action(('god_creation', 6))

                    # mortal deployment lane choices -- spawn the fighter created above in correct lane
                    elif g_deploy1.collidepoint(event.pos):
                        # gamePlayFunctions.god_troop_deploy(1)
                        send_action(('god_deploy', 1))
                    elif g_deploy2.collidepoint(event.pos):
                        # gamePlayFunctions.god_troop_deploy(2)
                        send_action(('god_deploy', 2))
                    elif g_deploy3.collidepoint(event.pos):
                        # gamePlayFunctions.god_troop_deploy(3)
                        send_action(('god_deploy', 3))
                    else:
                        g_tb_pressed = False
                        # if they didn't choose a valid deployment, nothing will happen

                    # Coin Upgrade Test
                    if g_coin_upgrade_b.collidepoint(event.pos):
                        gamePlayFunctions.god_coin_upgrade()
                        send_action(('coin_up_god', 'holder'))

                    if g_ability2_b.collidepoint(event.pos):
                        # god_heal_ability()
                        send_action(("god_heal", "holder"))

                    if g_ability1_b.collidepoint(event.pos):
                        gamePlayFunctions.lightning_pressed = True
                    elif ((top_lane.collidepoint(event.pos) or middle_lane.collidepoint(event.pos) or
                           bottom_lane.collidepoint(event.pos))):
                        if gamePlayFunctions.lightning_pressed:
                            lightning_attack(event.pos)
                    else:
                        gamePlayFunctions.lightning_pressed = False

        for mortal in mortal_list:
            # long-ranged attacks
            # check to see if any mortals got hit by an arrow/spell
            for spell in spell_list:
                gamePlayFunctions.ranged_hit(mortal, spell)

            # short range attacks
            # see if any monster in the lane is colliding
            for god in god_list:
                gamePlayFunctions.crash(mortal, god)

            # move the players
            if mortal.moving:
                mortal.move_right(mortal.speed)

            # attack the tower
            # if they've reached the tower already, but a troop is spawned to push them back
            if mortal.crash and mortal.hit_right_barrier:
                mortal.rect.x -= mortal.width
                mortal.hit_right_barrier = False
            elif mortal.hit_right_barrier:
                gamePlayFunctions.tower_damage("r", mortal)

            # reset crash and moving in case of defeat for next run
            mortal.crash = False
            mortal.moving = True

            # if the mortal is an archer, launch an arrow (delay based on elapsed time)
            if isinstance(mortal, Archer):
                if gamePlayFunctions.can_attack(mortal):
                    new_arrow = Arrow()
                    arrow_list.add(new_arrow)
                    new_arrow.rect.x = mortal.rect.x + mortal.width
                    new_arrow.rect.y = mortal.rect.y + mortal.height/2 - new_arrow.height/2

                    random_attack_delay = random.randint(mortal.attack_speed/2, mortal.attack_speed)
                    mortal.attack_time_counter = StateMachine.elapsed_time-mortal.spawn_time + random_attack_delay

        for god in god_list:
            for arrow in arrow_list:
                gamePlayFunctions.ranged_hit(god, arrow)

            if god.moving:
                god.move_left(god.speed)

            if god.crash and god.hit_left_barrier:
                god.rect.x += god.width
                god.hit_left_barrier = False
            if god.hit_left_barrier:
                gamePlayFunctions.tower_damage("l", god)

            god.crash = False
            god.moving = True

            if isinstance(god, Sorceress):
                if gamePlayFunctions.can_attack(god):
                    new_spell = Spell()
                    spell_list.add(new_spell)
                    new_spell.rect.x = god.rect.x - new_spell.width
                    new_spell.rect.y = god.rect.y + god.height/2 - new_spell.height/2

                    random_attack_delay = random.randint(god.attack_speed/2, god.attack_speed)
                    god.attack_time_counter = StateMachine.elapsed_time-god.spawn_time + random_attack_delay

        # move the arrows/spells and de-spawn them if they're out of range
        for arrow in arrow_list:
            arrow.move_right(arrow.speed)
            if arrow.halfway:
                arrow_list.remove(arrow)
        for spell in spell_list:
            spell.move_left(spell.speed)
            if spell.halfway:
                spell_list.remove(spell)

        for lightning in lightning_list:
            if StateMachine.elapsed_time - lightning.spawn_time >= lightning.life_span:
                print("l rem")
                lightning_list.remove(lightning)
            else:
                pygame.draw.circle(StateMachine.screen, StateMachine.BLACK, lightning.center, lightning.radius, 2)
        for catapult in catapult_list:
            if StateMachine.elapsed_time - catapult.spawn_time >= catapult.life_span:
                print("c rem")
                catapult_list.remove(catapult)
            else:
                pygame.draw.circle(StateMachine.screen, StateMachine.BLACK, catapult.center, catapult.radius, 2)

        # draw sprites
        mortal_list.draw(screen)
        god_list.draw(screen)
        arrow_list.draw(screen)
        spell_list.draw(screen)
        lightning_list.draw(screen)
        catapult_list.draw(screen)

        # update health labels (after .draw() so that it isn't overwritten)
        for mortal in mortal_list:
            mortal.update_health_label()
            mortal.update()
        for god in god_list:
            god.update_health_label()
            god.update()

    elif gamePlayFunctions.which_screen == "s":
        StateMachine.draw_start_menu()
        if not gamePlayFunctions.user_manual_stats_music:
            gamePlayFunctions.user_manual_stats_music = True
            music_unload_and_new("Music2.wav")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if mortal_rb.collidepoint(event.pos) and gamePlayFunctions.player_role == "d":
                    # change the role and send to the server so the other can be set
                    gamePlayFunctions.player_role = "m"
                    send_action(('mortal_chosen', "m"))
                if god_rb.collidepoint(event.pos) and gamePlayFunctions.player_role == "d":
                    gamePlayFunctions.player_role = "g"
                    send_action(('god_chosen', "g"))

                # start the game
                if start_b.collidepoint(event.pos):
                    send_action(("press_start", gamePlayFunctions.player_role))
                # display user manual/troop stats
                if manual_b.collidepoint(event.pos):
                    gamePlayFunctions.which_screen = "u"
                # quit game
                if quit_b.collidepoint(event.pos):
                    running = False

    elif gamePlayFunctions.which_screen == "c":
        StateMachine.draw_connection_screen()
        if not gamePlayFunctions.connection_music:
            gamePlayFunctions.connection_music = True
            music_unload_and_new("Music1.wav")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    StateMachine.ip_displayed = ""
                    StateMachine.input_box_active = True
                else:
                    StateMachine.input_box_active = False

                if get_ip_b.collidepoint(event.pos):
                    StateMachine.ip_displayed = localhost_ip
                if connect_b.collidepoint(event.pos):
                    gamePlayFunctions.which_screen = "s"
                    connect_to_server(StateMachine.ip_displayed)

            # This is how the input box text is changed by the user
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if StateMachine.input_box_active:
                        # store current text minus last char
                        StateMachine.ip_displayed = StateMachine.ip_displayed[:-1]
                else:
                    if StateMachine.input_box_active:
                        StateMachine.ip_displayed += event.unicode

    elif gamePlayFunctions.which_screen == "u":
        draw_manual_screen()
        if not gamePlayFunctions.user_manual_stats_music:
            gamePlayFunctions.user_manual_stats_music = True
            music_unload_and_new("Music2.wav")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_b.collidepoint(event.pos):
                    gamePlayFunctions.which_screen = "s"

    elif gamePlayFunctions.which_screen == "e":
        draw_end_screen()
        # music resets
        game_music = False
        connection_music = False
        start_music = False
        user_manual_stats_music = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_b.collidepoint(event.pos):
                    gamePlayFunctions.player_role = "d"
                    gamePlayFunctions.which_screen = "s"
                elif scores_b.collidepoint(event.pos):
                    gamePlayFunctions.which_screen = "b"
                elif e_quit_b.collidepoint(event.pos):
                    running = False

    elif gamePlayFunctions.which_screen == "b":
        draw_score_board()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_b.collidepoint(event.pos):
                    gamePlayFunctions.which_screen = "e"

    pygame.display.update()

# Wait for a few seconds before quitting
# pygame.time.wait(3000)
pygame.quit()
client.close()
sys.exit()
