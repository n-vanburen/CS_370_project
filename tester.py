import pygame
pygame.init()

# Canvas/Size
screen_size = (screen_w, screen_h) = (1200, 700)
canvas = pygame.display.set_mode(screen_size)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (150, 150, 150)

# Background
background_img = pygame.image.load('Background.png').convert()
background_img = pygame.transform.scale(background_img, screen_size)
canvas.blit(background_img, (0, 0))

# Towers
tower_size = (100, 100)
left_tower_dest = (25, 275)
right_tower_dest = (1075, 275)
tower_img = pygame.image.load('Tower.png').convert()
tower_img = pygame.transform.scale(tower_img, tower_size)
# Left
canvas.blit(tower_img, left_tower_dest)
left_tower_rect = pygame.draw.rect(canvas, BLACK, pygame.Rect(left_tower_dest, tower_size), 2)
# Right
canvas.blit(tower_img, right_tower_dest)
right_tower_rect = pygame.draw.rect(canvas, BLACK, pygame.Rect(right_tower_dest, tower_size), 2)

# Barrier Lines
left_barrier_coord = 210
right_barrier_coord = 990
# Left
pygame.draw.line(canvas, BLACK, (left_barrier_coord, 0), (left_barrier_coord, screen_h), 2)
# Right
pygame.draw.line(canvas, BLACK, (right_barrier_coord, 0), (right_barrier_coord, screen_h), 2)

# Center Top Timer Box
timer_coord = (500, 0)
timer_size = (200, 75)
timer = pygame.draw.rect(canvas, BLACK, pygame.Rect(timer_coord, timer_size), 2)

# Ability Buttons
# b = button, m = mortal, g = god
ability_size = (105, 105)
# Mortal
m_ability1_coord = (0, 0)
m_ability2_coord = (105, 0)
m_ability1_b = pygame.draw.rect(canvas, BLACK, pygame.Rect(m_ability1_coord, ability_size), 2)
m_ability2_b = pygame.draw.rect(canvas, BLACK, pygame.Rect(m_ability2_coord, ability_size), 2)
# God
g_ability1_coord = (990, 0)
g_ability2_coord = (1095, 0)
g_ability1_b = pygame.draw.rect(canvas, BLACK, pygame.Rect(g_ability1_coord, ability_size), 2)
g_ability2_b = pygame.draw.rect(canvas, BLACK, pygame.Rect(g_ability2_coord, ability_size), 2)

# Coins
coin_size = (80, 40)
# Mortal
m_coin_display_coord = (10, 520)
m_coin_upgrade_b_coord = (120, 520)
m_coin_display = pygame.draw.rect(canvas, BLACK, pygame.Rect(m_coin_display_coord, coin_size), 2)
m_coin_upgrade_b = pygame.draw.rect(canvas, BLACK, pygame.Rect(m_coin_upgrade_b_coord, coin_size), 2)
# God
g_coin_display_coord = (1000, 520)
g_coin_upgrade_b_coord = (1110, 520)
g_coin_display = pygame.draw.rect(canvas, BLACK, pygame.Rect(g_coin_display_coord, coin_size), 2)
g_coin_upgrade_b = pygame.draw.rect(canvas, BLACK, pygame.Rect(g_coin_upgrade_b_coord, coin_size), 2)

# Troop Spawn Buttons
# t = troop
tb_size = (70, 70)
tb_row1_y = 565
tb_row2_y = 635
# Mortal
m_tb_col1_x = 0
m_tb_col2_x = 70
m_tb_col3_x = 140
m_tb_1 = pygame.draw.rect(canvas, BLACK, pygame.Rect((m_tb_col1_x, tb_row1_y), tb_size), 2)
m_tb_2 = pygame.draw.rect(canvas, BLACK, pygame.Rect((m_tb_col2_x, tb_row1_y), tb_size), 2)
m_tb_3 = pygame.draw.rect(canvas, BLACK, pygame.Rect((m_tb_col3_x, tb_row1_y), tb_size), 2)
m_tb_4 = pygame.draw.rect(canvas, BLACK, pygame.Rect((m_tb_col1_x, tb_row2_y), tb_size), 2)
m_tb_5 = pygame.draw.rect(canvas, BLACK, pygame.Rect((m_tb_col2_x, tb_row2_y), tb_size), 2)
m_tb_6 = pygame.draw.rect(canvas, BLACK, pygame.Rect((m_tb_col3_x, tb_row2_y), tb_size), 2)
# God
g_tb_col1_x = 990
g_tb_col2_x = 1060
g_tb_col3_x = 1130
g_tb_1 = pygame.draw.rect(canvas, BLACK, pygame.Rect((g_tb_col1_x, tb_row1_y), tb_size), 2)
g_tb_2 = pygame.draw.rect(canvas, BLACK, pygame.Rect((g_tb_col2_x, tb_row1_y), tb_size), 2)
g_tb_3 = pygame.draw.rect(canvas, BLACK, pygame.Rect((g_tb_col3_x, tb_row1_y), tb_size), 2)
g_tb_4 = pygame.draw.rect(canvas, BLACK, pygame.Rect((g_tb_col1_x, tb_row2_y), tb_size), 2)
g_tb_5 = pygame.draw.rect(canvas, BLACK, pygame.Rect((g_tb_col2_x, tb_row2_y), tb_size), 2)
g_tb_6 = pygame.draw.rect(canvas, BLACK, pygame.Rect((g_tb_col3_x, tb_row2_y), tb_size), 2)

# Lanes
lane_size = (782, 100)
lane_left = 210
lane1_top = 175
lane2_top = 275
lane3_top = 375
top_lane = pygame.draw.rect(canvas, BLACK, pygame.Rect((lane_left, lane1_top), lane_size), 2)
middle_lane = pygame.draw.rect(canvas, BLACK, pygame.Rect((lane_left, lane2_top), lane_size), 2)
bottom_lane = pygame.draw.rect(canvas, BLACK, pygame.Rect((lane_left, lane3_top), lane_size), 2)

# Troop Deploy Zones - Week 4
t_deploy_size = (40, 98)
t_deploy1_top = 176
t_deploy2_top = 276
t_deploy3_top = 376
# Mortal
m_t_deploy_left = 170
m_deploy1 = pygame.draw.rect(canvas, GREY, pygame.Rect((m_t_deploy_left, t_deploy1_top), t_deploy_size))
m_deploy2 = pygame.draw.rect(canvas, GREY, pygame.Rect((m_t_deploy_left, t_deploy2_top), t_deploy_size))
m_deploy3 = pygame.draw.rect(canvas, GREY, pygame.Rect((m_t_deploy_left, t_deploy3_top), t_deploy_size))
# God
g_t_deploy_left = 992
g_deploy1 = pygame.draw.rect(canvas, GREY, pygame.Rect((g_t_deploy_left, t_deploy1_top), t_deploy_size))
g_deploy2 = pygame.draw.rect(canvas, GREY, pygame.Rect((g_t_deploy_left, t_deploy2_top), t_deploy_size))
g_deploy3 = pygame.draw.rect(canvas, GREY, pygame.Rect((g_t_deploy_left, t_deploy3_top), t_deploy_size))


# Title of Canvas
pygame.display.set_caption("My Board")

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
