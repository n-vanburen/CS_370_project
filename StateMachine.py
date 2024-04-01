import pygame
import gamePlayFunctions

pygame.init()

# Title of Canvas
pygame.display.set_caption("Lightning Town")

# Canvas/Size
screen_size = (screen_w, screen_h) = (1200, 700)
screen = pygame.display.set_mode(screen_size)

# fonts
main_font = pygame.font.SysFont("Font.ttf", 36)
fontCoins = pygame.font.Font("Font.ttf", 14)
title_font = pygame.font.SysFont("Font.tff", 75)
s_button_font = pygame.font.SysFont("Font.tff", 36)
ip_font = pygame.font.SysFont("Font.tff", 23)
fontCoinsUpgrade = pygame.font.Font("Font.ttf", 12)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (150, 150, 150)
MAIN_GREEN = (163, 188, 48)
SECOND_GREEN = (170, 225, 92)
THIRD_GREEN = (217, 231, 129)

# Background
background_img = pygame.image.load('Background.png').convert()
background_img = pygame.transform.scale(background_img, screen_size)


def load_background():
    screen.blit(background_img, (0, 0))


# main game board:
# Towers
tower_size = (100, 100)
left_tower_dest = (25, 275)
right_tower_dest = (1075, 275)
tower_img = pygame.image.load('Tower.png').convert()
tower_img = pygame.transform.scale(tower_img, tower_size)
left_tower_rect = pygame.Rect(left_tower_dest, tower_size)
right_tower_rect = pygame.Rect(right_tower_dest, tower_size)
left_tower_health = 100
right_tower_health = 100

# Barrier Lines
left_barrier_coord = 210
right_barrier_coord = 990

# Center Top Timer Box
timer_coord = (500, 0)
timer_size = (200, 75)
timer = pygame.Rect(timer_coord, timer_size)
# Timer Game variables
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()  # Get the starting time of the game
game_duration = 5 * 60 * 1000 + 1000  # 5 minutes in milliseconds
timed_out = False
elapsed_time = 0

# Ability Buttons
# b = button, m = mortal, g = god
ability_size = (105, 105)
# Mortal
m_ability1_coord = (0, 0)
m_ability2_coord = (105, 0)
m_ability1_b = pygame.Rect(m_ability1_coord, ability_size)
m_ability2_b = pygame.Rect(m_ability2_coord, ability_size)
# God
g_ability1_coord = (990, 0)
g_ability2_coord = (1095, 0)
g_ability1_b = pygame.Rect(g_ability1_coord, ability_size)
g_ability2_b = pygame.Rect(g_ability2_coord, ability_size)

# Coins
coin_size = (coin_w, coin_h) = (80, 40)
one_second_tracker = 1000
# Mortal's initial balance/level
mortals_coins = 50
mortal_coin_level = 1
# Mortal
m_coin_display_coord = (10, 520)
m_coin_upgrade_b_coord = (120, 520)
m_coin_display = pygame.Rect(m_coin_display_coord, coin_size)
m_coin_upgrade_b = pygame.Rect(m_coin_upgrade_b_coord, coin_size)
# God's initial coin balance/level
gods_coins = 50
god_coin_level = 1
# God
g_coin_display_coord = (1000, 520)
g_coin_upgrade_b_coord = (1110, 520)
g_coin_display = pygame.Rect(g_coin_display_coord, coin_size)
g_coin_upgrade_b = pygame.Rect(g_coin_upgrade_b_coord, coin_size)

# Troop Spawn Buttons
# tb = troop button
tb_size = (tb_width, tb_height) = (70, 70)
tb_row1_y = 565
tb_row2_y = 635
# Mortal
m_tb_col1_x = 0
m_tb_col2_x = 70
m_tb_col3_x = 140
m_tb_1 = pygame.Rect((m_tb_col1_x, tb_row1_y), tb_size)
m_tb_2 = pygame.Rect((m_tb_col2_x, tb_row1_y), tb_size)
m_tb_3 = pygame.Rect((m_tb_col3_x, tb_row1_y), tb_size)
m_tb_4 = pygame.Rect((m_tb_col1_x, tb_row2_y), tb_size)
m_tb_5 = pygame.Rect((m_tb_col2_x, tb_row2_y), tb_size)
m_tb_6 = pygame.Rect((m_tb_col3_x, tb_row2_y), tb_size)
# God
g_tb_col1_x = 990
g_tb_col2_x = 1060
g_tb_col3_x = 1130
g_tb_1 = pygame.Rect((g_tb_col1_x, tb_row1_y), tb_size)
g_tb_2 = pygame.Rect((g_tb_col2_x, tb_row1_y), tb_size)
g_tb_3 = pygame.Rect((g_tb_col3_x, tb_row1_y), tb_size)
g_tb_4 = pygame.Rect((g_tb_col1_x, tb_row2_y), tb_size)
g_tb_5 = pygame.Rect((g_tb_col2_x, tb_row2_y), tb_size)
g_tb_6 = pygame.Rect((g_tb_col3_x, tb_row2_y), tb_size)

# Lanes
lane_size = (782, 100)
lane_left = 210
lane1_top = 175
lane2_top = 275
lane3_top = 375
top_lane = pygame.Rect((lane_left, lane1_top), lane_size)
middle_lane = pygame.Rect((lane_left, lane2_top), lane_size)
bottom_lane = pygame.Rect((lane_left, lane3_top), lane_size)

# Troop Deploy Zones
t_deploy_size = (t_deploy_width, t_deploy_height) = (40, 98)
t_deploy1_top = 176
t_deploy2_top = 276
t_deploy3_top = 376
# Mortal
m_t_deploy_left = 170
m_deploy1 = pygame.Rect((m_t_deploy_left, t_deploy1_top), t_deploy_size)
m_deploy2 = pygame.Rect((m_t_deploy_left, t_deploy2_top), t_deploy_size)
m_deploy3 = pygame.Rect((m_t_deploy_left, t_deploy3_top), t_deploy_size)
# God
g_t_deploy_left = 992
g_deploy1 = pygame.Rect((g_t_deploy_left, t_deploy1_top), t_deploy_size)
g_deploy2 = pygame.Rect((g_t_deploy_left, t_deploy2_top), t_deploy_size)
g_deploy3 = pygame.Rect((g_t_deploy_left, t_deploy3_top), t_deploy_size)


# Function to draw the main game screen
def draw_game_screen():
    global elapsed_time
    global timed_out
    global one_second_tracker
    global mortals_coins
    global gods_coins
    global elapsed_time

    load_background()

    # Towers
    # Left
    screen.blit(tower_img, left_tower_dest)
    pygame.draw.rect(screen, BLACK, left_tower_rect, 2)
    left_tower_text_surface = main_font.render(str(left_tower_health), True, BLACK)
    left_tower_health_dest = ((left_tower_rect.x + left_tower_rect.w) - (left_tower_text_surface.get_width()+3),
                              (left_tower_rect.y + left_tower_rect.h) - left_tower_text_surface.get_height())
    screen.blit(left_tower_text_surface, left_tower_health_dest)
    # Right
    screen.blit(tower_img, right_tower_dest)
    pygame.draw.rect(screen, BLACK, right_tower_rect, 2)
    right_tower_text_surface = main_font.render(str(right_tower_health), True, BLACK)
    right_tower_health_dest = ((right_tower_rect.x + right_tower_rect.w) - (right_tower_text_surface.get_width()+3),
                               (right_tower_rect.y + right_tower_rect.h) - right_tower_text_surface.get_height())
    screen.blit(right_tower_text_surface, right_tower_health_dest)

    # Barrier Lines
    # Left
    pygame.draw.line(screen, BLACK, (left_barrier_coord, 0), (left_barrier_coord, screen_h), 2)
    # Right
    pygame.draw.line(screen, BLACK, (right_barrier_coord, 0), (right_barrier_coord, screen_h), 2)

    # Center Top Timer Box
    pygame.draw.rect(screen, SECOND_GREEN, timer)
    pygame.draw.rect(screen, BLACK, timer, 2)

    # Ability Buttons
    # Mortal
    pygame.draw.rect(screen, THIRD_GREEN, m_ability1_b)
    pygame.draw.rect(screen, THIRD_GREEN, m_ability2_b)
    pygame.draw.rect(screen, BLACK, m_ability1_b, 2)
    pygame.draw.rect(screen, BLACK, m_ability2_b, 2)
    # God
    pygame.draw.rect(screen, THIRD_GREEN, g_ability1_b)
    pygame.draw.rect(screen, THIRD_GREEN, g_ability2_b)
    pygame.draw.rect(screen, BLACK, g_ability1_b, 2)
    pygame.draw.rect(screen, BLACK, g_ability2_b, 2)

    # Coins
    # Mortal
    if gamePlayFunctions.player_role == "m":
        pygame.draw.rect(screen, SECOND_GREEN, m_coin_display)
        pygame.draw.rect(screen, SECOND_GREEN, m_coin_upgrade_b)
    else:
        pygame.draw.rect(screen, BLACK, m_coin_display)
        pygame.draw.rect(screen, BLACK, m_coin_upgrade_b)
    pygame.draw.rect(screen, BLACK, m_coin_display, 2)
    pygame.draw.rect(screen, BLACK, m_coin_upgrade_b, 2)
    # God
    if gamePlayFunctions.player_role == "g":
        pygame.draw.rect(screen, SECOND_GREEN, g_coin_display)
        pygame.draw.rect(screen, SECOND_GREEN, g_coin_upgrade_b)
    else:
        pygame.draw.rect(screen, BLACK, g_coin_display)
        pygame.draw.rect(screen, BLACK, g_coin_upgrade_b)
    pygame.draw.rect(screen, BLACK, g_coin_display, 2)
    pygame.draw.rect(screen, BLACK, g_coin_upgrade_b, 2)
    # Troop Spawn Buttons
    # Mortal
    pygame.draw.rect(screen, THIRD_GREEN, m_tb_1)
    pygame.draw.rect(screen, THIRD_GREEN, m_tb_3)
    pygame.draw.rect(screen, THIRD_GREEN, m_tb_2)
    pygame.draw.rect(screen, THIRD_GREEN, m_tb_4)
    pygame.draw.rect(screen, THIRD_GREEN, m_tb_5)
    pygame.draw.rect(screen, THIRD_GREEN, m_tb_6)
    pygame.draw.rect(screen, BLACK, m_tb_1, 2)
    pygame.draw.rect(screen, BLACK, m_tb_2, 2)
    pygame.draw.rect(screen, BLACK, m_tb_3, 2)
    pygame.draw.rect(screen, BLACK, m_tb_4, 2)
    pygame.draw.rect(screen, BLACK, m_tb_5, 2)
    pygame.draw.rect(screen, BLACK, m_tb_6, 2)
    # God
    pygame.draw.rect(screen, THIRD_GREEN, g_tb_1)
    pygame.draw.rect(screen, THIRD_GREEN, g_tb_2)
    pygame.draw.rect(screen, THIRD_GREEN, g_tb_3)
    pygame.draw.rect(screen, THIRD_GREEN, g_tb_4)
    pygame.draw.rect(screen, THIRD_GREEN, g_tb_5)
    pygame.draw.rect(screen, THIRD_GREEN, g_tb_6)
    pygame.draw.rect(screen, BLACK, g_tb_1, 2)
    pygame.draw.rect(screen, BLACK, g_tb_2, 2)
    pygame.draw.rect(screen, BLACK, g_tb_3, 2)
    pygame.draw.rect(screen, BLACK, g_tb_4, 2)
    pygame.draw.rect(screen, BLACK, g_tb_5, 2)
    pygame.draw.rect(screen, BLACK, g_tb_6, 2)
    # Lanes
    pygame.draw.rect(screen, MAIN_GREEN, top_lane)
    pygame.draw.rect(screen, MAIN_GREEN, middle_lane)
    pygame.draw.rect(screen, MAIN_GREEN, bottom_lane)
    pygame.draw.rect(screen, BLACK, top_lane, 2)
    pygame.draw.rect(screen, BLACK, middle_lane, 2)
    pygame.draw.rect(screen, BLACK, bottom_lane, 2)

    # Troop Deploy Zones
    # Mortal
    pygame.draw.rect(screen, GREY, m_deploy1)
    pygame.draw.rect(screen, GREY, m_deploy2)
    pygame.draw.rect(screen, GREY, m_deploy3)
    # God
    pygame.draw.rect(screen, GREY, g_deploy1)
    pygame.draw.rect(screen, GREY, g_deploy2)
    pygame.draw.rect(screen, GREY, g_deploy3)

    # Calculate elapsed time
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time

    # Convert milliseconds to minutes and seconds
    minutes = (game_duration - elapsed_time) // 60000
    seconds = ((game_duration - elapsed_time) // 1000) % 60

    # Render the timer text
    timer_text = f"Time Left: {minutes:02}:{seconds:02}"

    if elapsed_time >= game_duration:
        timed_out = True
        timer_text = "Time Left: 00:00"

    timer_surface = main_font.render(timer_text, True, BLACK)
    screen.blit(timer_surface, (507, 20))

    # Generate coins every second
    if one_second_tracker <= elapsed_time:
        if mortal_coin_level == 1:
            mortals_coins += 10
        elif mortal_coin_level == 2:
            mortals_coins += 25
        elif mortal_coin_level == 3:
            mortals_coins += 50
        if god_coin_level == 1:
            gods_coins += 10
        elif god_coin_level == 2:
            gods_coins += 25
        elif god_coin_level == 3:
            gods_coins += 50
        one_second_tracker += 1000

    # Display to screen current coins
    mortal_coin_text = fontCoins.render(f"Coins: {mortals_coins}", True, (0, 0, 0))
    screen.blit(mortal_coin_text, (m_coin_display.x+4, m_coin_display.y+6))
    gods_coin_text = fontCoins.render(f"Coins: {gods_coins}", True, (0, 0, 0))
    screen.blit(gods_coin_text, (g_coin_display.x+4, g_coin_display.y+6))

    # Display to screen current levels and upgrade cost
    mortal_coin_level_text = fontCoins.render(f"Level: {mortal_coin_level}", True, (0, 0, 0))
    screen.blit(mortal_coin_level_text, (m_coin_upgrade_b.x+16, m_coin_upgrade_b.y))
    god_coin_level_text = fontCoins.render(f"Level: {god_coin_level}", True, (0, 0, 0))
    screen.blit(god_coin_level_text, (g_coin_upgrade_b.x+16, g_coin_upgrade_b.y))
    if god_coin_level == 1:
        g_upgrade_cost = 300
    elif god_coin_level == 2:
        g_upgrade_cost = 500
    else:
        g_upgrade_cost = 0
        # impossible but IDE complaining
    if mortal_coin_level == 1:
        m_upgrade_cost = 300
    elif mortal_coin_level == 2:
        m_upgrade_cost = 500
    else:
        m_upgrade_cost = 0
        # impossible but IDE complaining

    if mortal_coin_level < 3:
        mortal_coin_upgrade_text = fontCoinsUpgrade.render(f"Upgrade: {m_upgrade_cost}", True, (0, 0, 0))
        screen.blit(mortal_coin_upgrade_text, (m_coin_upgrade_b.x+2, m_coin_upgrade_b.y+16))
    if god_coin_level < 3:
        god_coin_upgrade_text = fontCoinsUpgrade.render(f"Upgrade: {g_upgrade_cost}", True, (0, 0, 0))
        screen.blit(god_coin_upgrade_text, (g_coin_upgrade_b.x+2, g_coin_upgrade_b.y+16))


# Main box for the start menu
main_menu_rect = pygame.Rect(screen_w/4, screen_h/16, screen_w/2, screen_h*0.875)

# game title
title_text_surface = title_font.render("Lightning Town!", True, BLACK)
title_text_dest = (((main_menu_rect.left + main_menu_rect.w/2) - title_text_surface.get_width()/2),
                   main_menu_rect.top + 50)

# buttons
s_button_size = (s_button_w, s_button_h) = (200, 50)

# for player to choose their role (mortal or god) rb = role button
mortal_rb = pygame.Rect(((main_menu_rect.left+main_menu_rect.w/2-s_button_w),
                         (main_menu_rect.top+title_text_surface.get_height()+main_menu_rect.h/8+25)), s_button_size)
mortal_rb_text_surface = s_button_font.render("Mortal", True, BLACK)
mortal_rb_text_dest = (((mortal_rb.left+mortal_rb.w/2)-mortal_rb_text_surface.get_width()/2),
                       ((mortal_rb.top+mortal_rb.h/2)-mortal_rb_text_surface.get_height()/2))
god_rb = pygame.Rect(((main_menu_rect.left+main_menu_rect.w/2), mortal_rb.top), s_button_size)
god_rb_text_surface = s_button_font.render("God", True, BLACK)
god_rb_text_dest = (((god_rb.left+god_rb.w/2)-god_rb_text_surface.get_width()/2),
                    ((god_rb.top+god_rb.h/2)-god_rb_text_surface.get_height()/2))

start_b = pygame.Rect(((main_menu_rect.left+main_menu_rect.w/2-s_button_w/2),
                       (mortal_rb.top+s_button_h+main_menu_rect.h/10)), s_button_size)
stats_b = pygame.Rect((start_b.left, start_b.top+s_button_h+main_menu_rect.h/10), s_button_size)
quit_b = pygame.Rect((stats_b.left, stats_b.top+s_button_h+main_menu_rect.h/10), s_button_size)

# button text
start_b_text_surface = s_button_font.render("Start", True, BLACK)
stats_b_text_surface = s_button_font.render("User Manual", True, BLACK)
quit_b_text_surface = s_button_font.render("Quit", True, BLACK)

start_b_text_dest = (((start_b.left+start_b.w/2)-start_b_text_surface.get_width()/2),
                     ((start_b.top+start_b.h/2)-start_b_text_surface.get_height()/2))
stats_b_text_dest = (((stats_b.left+stats_b.w/2)-stats_b_text_surface.get_width()/2),
                     ((stats_b.top+stats_b.h/2)-stats_b_text_surface.get_height()/2))
quit_b_text_dest = (((quit_b.left+quit_b.w/2)-quit_b_text_surface.get_width()/2),
                    ((quit_b.top+quit_b.h/2)-quit_b_text_surface.get_height()/2))


def draw_start_menu():
    global mortal_rb_text_surface
    global god_rb_text_surface

    load_background()

    # main box
    pygame.draw.rect(screen, MAIN_GREEN, main_menu_rect)
    pygame.draw.rect(screen, BLACK, main_menu_rect, 2)

    # game title
    screen.blit(title_text_surface, title_text_dest)

    # role choice buttons
    if gamePlayFunctions.player_role == "m" or gamePlayFunctions.player_role == "d":
        pygame.draw.rect(screen, THIRD_GREEN, mortal_rb)
        mortal_rb_text_surface = s_button_font.render("Mortal", True, BLACK)
    else:
        pygame.draw.rect(screen, BLACK, mortal_rb)
        mortal_rb_text_surface = s_button_font.render("Mortal", True, THIRD_GREEN)

    if gamePlayFunctions.player_role == "g" or gamePlayFunctions.player_role == "d":
        pygame.draw.rect(screen, THIRD_GREEN, god_rb)
        god_rb_text_surface = s_button_font.render("God", True, BLACK)
    else:
        pygame.draw.rect(screen, BLACK, god_rb)
        god_rb_text_surface = s_button_font.render("God", True, THIRD_GREEN)

    pygame.draw.rect(screen, BLACK, mortal_rb, 2)
    screen.blit(mortal_rb_text_surface, mortal_rb_text_dest)
    pygame.draw.rect(screen, BLACK, god_rb, 2)
    screen.blit(god_rb_text_surface, god_rb_text_dest)

    # buttons
    pygame.draw.rect(screen, THIRD_GREEN, start_b)
    pygame.draw.rect(screen, BLACK, start_b, 2)
    pygame.draw.rect(screen, THIRD_GREEN, stats_b)
    pygame.draw.rect(screen, BLACK, stats_b, 2)
    pygame.draw.rect(screen, THIRD_GREEN, quit_b)
    pygame.draw.rect(screen, BLACK, quit_b, 2)

    # button text
    screen.blit(start_b_text_surface, start_b_text_dest)
    screen.blit(stats_b_text_surface, stats_b_text_dest)
    screen.blit(quit_b_text_surface, quit_b_text_dest)


# a different screen. This one is used to connect to the server/other client and choose the player's role
connection_box = pygame.Rect(screen_w/4, screen_h/4, screen_w/2, screen_h/2)

# box for user to enter or view IP address
input_box_size = (ibw, ibh) = s_button_size
input_box = pygame.Rect((((connection_box.left+connection_box.w/2)-ibw/2),
                         ((connection_box.top+title_text_surface.get_height()+connection_box.h/5)-ibh/2)),
                        input_box_size)
ip_displayed = "Enter Server IP"
input_box_active = False

# buttons for the user to either get their personal IP or connect to an entered IP
# ip_b_size = (ipw, iph) = (100, 40)
get_ip_b = pygame.Rect((input_box.left, (input_box.top+ibh+20)), s_button_size)
connect_b = pygame.Rect((input_box.left, (get_ip_b.top+ibh+20)), s_button_size)

# text for hosting server and connecting buttons
get_ip_text_surface = s_button_font.render("Host Server", True, BLACK)
get_ip_text_dest = (((get_ip_b.left+get_ip_b.w/2)-get_ip_text_surface.get_width()/2),
                    ((get_ip_b.top+get_ip_b.h/2)-get_ip_text_surface.get_height()/2))
connect_text_surface = s_button_font.render("Connect", True, BLACK)
connect_text_dest = (((connect_b.left+connect_b.w/2)-connect_text_surface.get_width()/2),
                     ((connect_b.top+connect_b.h/2)-connect_text_surface.get_height()/2))


def draw_connection_screen():
    global ip_displayed

    load_background()

    # main box
    pygame.draw.rect(screen, MAIN_GREEN, connection_box)
    pygame.draw.rect(screen, BLACK, connection_box, 2)

    # title
    screen.blit(title_text_surface, (((connection_box.left + connection_box.w/2) - title_text_surface.get_width()/2),
                                     connection_box.top + 20))

    # input box for IP
    pygame.draw.rect(screen, THIRD_GREEN, input_box)
    pygame.draw.rect(screen, BLACK, input_box, 2)

    input_box_text_surface = s_button_font.render(ip_displayed, True, BLACK)
    input_box_text_dest = (((input_box.left+input_box.w/2)-input_box_text_surface.get_width()/2),
                           ((input_box.top+input_box.h/2)-input_box_text_surface.get_height()/2))
    screen.blit(input_box_text_surface, input_box_text_dest)

    # get ip and connect buttons
    pygame.draw.rect(screen, THIRD_GREEN, get_ip_b)
    pygame.draw.rect(screen, BLACK, get_ip_b, 2)
    screen.blit(get_ip_text_surface, get_ip_text_dest)
    pygame.draw.rect(screen, THIRD_GREEN, connect_b)
    pygame.draw.rect(screen, BLACK, connect_b, 2)
    screen.blit(connect_text_surface, connect_text_dest)


# Stats screen
# image that displays the user manual
user_manual_img = pygame.image.load('user_manual.png')
user_manual_img_size = (umw, umh) = (user_manual_img.get_width()*0.85, user_manual_img.get_height()*0.85)
user_manual_img = pygame.transform.scale(user_manual_img, (umw, umh))

# main box
stats_main_box = pygame.Rect(screen_w/2-umw/2, screen_h/2-umh/2, umw, umh)

# back button
back_b = pygame.Rect(25, 25, 100, 50)
back_b_text_surface = s_button_font.render("<- Back", True, BLACK)
back_b_text_dest = (((back_b.left+back_b.w/2)-back_b_text_surface.get_width()/2),
                    ((back_b.top+back_b.h/2)-back_b_text_surface.get_height()/2))


def draw_stats_screen():
    load_background()

    pygame.draw.rect(screen, MAIN_GREEN, stats_main_box)
    pygame.draw.rect(screen, BLACK, stats_main_box, 2)

    pygame.draw.rect(screen, THIRD_GREEN, back_b)
    pygame.draw.rect(screen, BLACK, back_b, 2)
    screen.blit(back_b_text_surface, back_b_text_dest)

    # pygame.Surface.set_colorkey(user_manual_img, (255, 255, 255))
    screen.blit(user_manual_img, (stats_main_box.left, stats_main_box.top))


# end menu
# main box -- same size as start menu, reuse main_menu_rect
# winner text
winner = "Mortals Win!"
winner_text_surface = title_font.render(winner, True, BLACK)
winner_text_dest = (((main_menu_rect.left + main_menu_rect.w/2) - winner_text_surface.get_width()/2),
                    main_menu_rect.top + 50)

# play again button
play_b = pygame.Rect(((main_menu_rect.left+main_menu_rect.w/2-s_button_w/2),
                      (main_menu_rect.top+winner_text_surface.get_height()+main_menu_rect.h/8+50)), s_button_size)
play_b_text_surface = s_button_font.render("Play Again", True, BLACK)
play_b_text_dest = (((play_b.left+play_b.w/2)-play_b_text_surface.get_width()/2),
                    ((play_b.top+play_b.h/2)-play_b_text_surface.get_height()/2))

# new opponent button
new_opp_b = pygame.Rect((play_b.left, play_b.top+s_button_h+main_menu_rect.h/8), s_button_size)
new_opp_b_text_surface = s_button_font.render("New Opponent", True, BLACK)
new_opp_b_text_dest = (((new_opp_b.left+new_opp_b.w/2)-new_opp_b_text_surface.get_width()/2),
                       ((new_opp_b.top+new_opp_b.h/2)-new_opp_b_text_surface.get_height()/2))

# scoreboard button (if we have it, change /8 to /10 and add 25 on play_b not 50)
# scores_b = pygame.Rect((new_opp_b.left, new_opp_b.top+s_button_h+main_menu_rect.h/10), s_button_size)
# scores_b_text_surface = s_button_font.render("Scoreboard", True, BLACK)
# scores_b_text_dest = (((scores_b.left+scores_b.w/2)-scores_b_text_surface.get_width()/2),
#                      ((scores_b.top+scores_b.h/2)-scores_b_text_surface.get_height()/2))

# quit button
e_quit_b = pygame.Rect((new_opp_b.left, new_opp_b.top+s_button_h+main_menu_rect.h/8), s_button_size)
e_quit_b_text_surface = s_button_font.render("Quit", True, BLACK)
e_quit_b_text_dest = (((e_quit_b.left+e_quit_b.w/2)-e_quit_b_text_surface.get_width()/2),
                      ((e_quit_b.top+e_quit_b.h/2)-e_quit_b_text_surface.get_height()/2))


def draw_end_screen():
    global winner
    global winner_text_surface
    global winner_text_dest

    load_background()

    pygame.draw.rect(screen, MAIN_GREEN, main_menu_rect)
    pygame.draw.rect(screen, BLACK, main_menu_rect, 2)

    winner_text_surface = title_font.render(winner, True, BLACK)
    winner_text_dest = (((main_menu_rect.left + main_menu_rect.w/2) - winner_text_surface.get_width()/2),
                        main_menu_rect.top + 50)
    screen.blit(winner_text_surface, winner_text_dest)

    pygame.draw.rect(screen, THIRD_GREEN, play_b)
    pygame.draw.rect(screen, BLACK, play_b, 2)
    screen.blit(play_b_text_surface, play_b_text_dest)

    pygame.draw.rect(screen, THIRD_GREEN, new_opp_b)
    pygame.draw.rect(screen, BLACK, new_opp_b, 2)
    screen.blit(new_opp_b_text_surface, new_opp_b_text_dest)

    # pygame.draw.rect(screen, THIRD_GREEN, scores_b)
    # pygame.draw.rect(screen, BLACK, scores_b, 2)
    # screen.blit(scores_b_text_surface, scores_b_text_dest)

    pygame.draw.rect(screen, THIRD_GREEN, e_quit_b)
    pygame.draw.rect(screen, BLACK, e_quit_b, 2)
    screen.blit(e_quit_b_text_surface, e_quit_b_text_dest)
