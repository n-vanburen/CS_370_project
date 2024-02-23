import pygame
import sys

pygame.init()

# Canvas/Size
screen_size = (screen_w, screen_h) = (1200, 700)
screen = pygame.display.set_mode(screen_size)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (150, 150, 150)

# Background
background_img = pygame.image.load('Background.png').convert()
background_img = pygame.transform.scale(background_img, screen_size)

# variables for use in other files
# Towers
tower_size = (100, 100)
left_tower_dest = (25, 275)
right_tower_dest = (1075, 275)
tower_img = pygame.image.load('Tower.png').convert()
tower_img = pygame.transform.scale(tower_img, tower_size)
left_tower_rect = pygame.Rect(left_tower_dest, tower_size)
right_tower_rect = pygame.Rect(right_tower_dest, tower_size)

# Barrier Lines
left_barrier_coord = 210
right_barrier_coord = 990

# Center Top Timer Box
timer_coord = (500, 0)
timer_size = (200, 75)
timer = pygame.Rect(timer_coord, timer_size)
# Timer Fonts
font = pygame.font.SysFont("Font.tff", 36)
# Timer Game variables
# Main game loop timer
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()  # Get the starting time of the game
game_duration = 5 * 60 * 1000  # 5 minutes in milliseconds
timed_out = False

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
coin_size = (80, 40)
# Mortal
m_coin_display_coord = (10, 520)
m_coin_upgrade_b_coord = (120, 520)
m_coin_display = pygame.Rect(m_coin_display_coord, coin_size)
m_coin_upgrade_b = pygame.Rect(m_coin_upgrade_b_coord, coin_size)
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


def load_background():
    screen.blit(background_img, (0, 0))


# Function to draw the main game screen
def draw_game_screen():
    global timed_out

    load_background()

    # Towers
    # Left
    screen.blit(tower_img, left_tower_dest)
    pygame.draw.rect(screen, BLACK, left_tower_rect, 2)
    # Right
    screen.blit(tower_img, right_tower_dest)
    pygame.draw.rect(screen, BLACK, right_tower_rect, 2)

    # Barrier Lines
    # Left
    pygame.draw.line(screen, BLACK, (left_barrier_coord, 0), (left_barrier_coord, screen_h), 2)
    # Right
    pygame.draw.line(screen, BLACK, (right_barrier_coord, 0), (right_barrier_coord, screen_h), 2)

    # Center Top Timer Box
    pygame.draw.rect(screen, BLACK, timer, 2)

    # Ability Buttons
    # Mortal
    pygame.draw.rect(screen, BLACK, m_ability1_b, 2)
    pygame.draw.rect(screen, BLACK, m_ability2_b, 2)
    # God
    pygame.draw.rect(screen, BLACK, g_ability1_b, 2)
    pygame.draw.rect(screen, BLACK, g_ability2_b, 2)

    # Coins
    # Mortal
    pygame.draw.rect(screen, BLACK, m_coin_display, 2)
    pygame.draw.rect(screen, BLACK, m_coin_upgrade_b, 2)
    # God
    pygame.draw.rect(screen, BLACK, g_coin_display, 2)
    pygame.draw.rect(screen, BLACK, g_coin_upgrade_b, 2)

    # Troop Spawn Buttons
    # Mortal
    pygame.draw.rect(screen, BLACK, m_tb_1, 2)
    pygame.draw.rect(screen, BLACK, m_tb_2, 2)
    pygame.draw.rect(screen, BLACK, m_tb_3, 2)
    pygame.draw.rect(screen, BLACK, m_tb_4, 2)
    pygame.draw.rect(screen, BLACK, m_tb_5, 2)
    pygame.draw.rect(screen, BLACK, m_tb_6, 2)
    # God
    pygame.draw.rect(screen, BLACK, g_tb_1, 2)
    pygame.draw.rect(screen, BLACK, g_tb_2, 2)
    pygame.draw.rect(screen, BLACK, g_tb_3, 2)
    pygame.draw.rect(screen, BLACK, g_tb_4, 2)
    pygame.draw.rect(screen, BLACK, g_tb_5, 2)
    pygame.draw.rect(screen, BLACK, g_tb_6, 2)

    # Lanes
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
    # elapsed_time = 10000

    # Convert milliseconds to minutes and seconds
    minutes = (game_duration - elapsed_time) // 60000
    seconds = ((game_duration - elapsed_time) // 1000) % 60

    # Render the timer text
    timer_text = f"Time Left: {minutes:02}:{seconds:02}"

    if elapsed_time >= game_duration:
        timed_out = True
        timer_text = "Time Left: 00:00"

    timer_surface = font.render(timer_text, True, BLACK)
    screen.blit(timer_surface, (507, 20))


# Title of Canvas
pygame.display.set_caption("Lightning Town")