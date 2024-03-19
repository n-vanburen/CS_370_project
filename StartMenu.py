# import pygame
from gameBoard import *

# Main box for the start menu
main_menu_rect = pygame.Rect(screen_w/4, screen_h/16, screen_w/2, screen_h*0.875)

# game title
title_font = pygame.font.SysFont("Font.tff", 75)
title_text_surface = title_font.render("Lightning Town!", True, BLACK)
title_text_dest = (((main_menu_rect.left + main_menu_rect.w/2) - title_text_surface.get_width()/2),
                   main_menu_rect.top + 50)

# buttons
s_button_size = (s_button_w, s_button_h) = (200, 50)
start_b = pygame.Rect(((main_menu_rect.left+main_menu_rect.w/2-s_button_w/2),
                      (main_menu_rect.top+title_text_surface.get_height()+main_menu_rect.h/8+50)), s_button_size)
stats_b = pygame.Rect((start_b.left, start_b.top+s_button_h+main_menu_rect.h/8), s_button_size)
quit_b = pygame.Rect((stats_b.left, stats_b.top+s_button_h+main_menu_rect.h/8), s_button_size)

# button text
s_button_font = pygame.font.SysFont("Font.tff", 36)
start_b_text_surface = s_button_font.render("Start", True, BLACK)
stats_b_text_surface = s_button_font.render("User Manual", True, BLACK)
quit_b_text_surface = s_button_font.render("Quit", True, BLACK)

start_b_text_dest = (((start_b.left+start_b.w/2)-start_b_text_surface.get_width()/2),
                     ((start_b.top+start_b.h/2)-start_b_text_surface.get_height()/2))
stats_b_text_dest = (((stats_b.left+stats_b.w/2)-stats_b_text_surface.get_width()/2),
                     ((stats_b.top+stats_b.h/2)-stats_b_text_surface.get_height()/2))
quit_b_text_dest = (((quit_b.left+quit_b.w/2)-quit_b_text_surface.get_width()/2),
                    ((quit_b.top+quit_b.h/2)-quit_b_text_surface.get_height()/2))


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
ip_b_size = (ipw, iph) = (100, 40)
get_ip_b = pygame.Rect((((connection_box.left+connection_box.w/2)-(ipw+20)),
                        (input_box.top+ibh+10)), ip_b_size)
connect_b = pygame.Rect((((connection_box.left+connection_box.w/2)+20),
                         (input_box.top+ibh+10)), ip_b_size)

# text for hosting server and connecting buttons
ip_font = pygame.font.SysFont("Font.tff", 23)
get_ip_text_surface = ip_font.render("Host Server", True, BLACK)
get_ip_text_dest = (((get_ip_b.left+get_ip_b.w/2)-get_ip_text_surface.get_width()/2),
                    ((get_ip_b.top+get_ip_b.h/2)-get_ip_text_surface.get_height()/2))
connect_text_surface = ip_font.render("Connect", True, BLACK)
connect_text_dest = (((connect_b.left+connect_b.w/2)-connect_text_surface.get_width()/2),
                     ((connect_b.top+connect_b.h/2)-connect_text_surface.get_height()/2))

# buttons for player to choose their role (mortal or god) rb = role button
mortal_rb = pygame.Rect((((connection_box.left+connection_box.w/4)-ibw/2),
                        (input_box.top+ibh+connection_box.h/4)), input_box_size)
mortal_rb_text_surface = s_button_font.render("Mortal", True, BLACK)
mortal_rb_text_dest = (((mortal_rb.left+mortal_rb.w/2)-mortal_rb_text_surface.get_width()/2),
                       ((mortal_rb.top+mortal_rb.h/2)-mortal_rb_text_surface.get_height()/2))
god_rb = pygame.Rect((((connection_box.left+connection_box.w*0.75)-ibw/2),
                      (input_box.top+ibh+connection_box.h/4)), input_box_size)
god_rb_text_surface = s_button_font.render("God", True, BLACK)
god_rb_text_dest = (((god_rb.left+god_rb.w/2)-god_rb_text_surface.get_width()/2),
                    ((god_rb.top+god_rb.h/2)-god_rb_text_surface.get_height()/2))


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

    # role choice buttons
    pygame.draw.rect(screen, THIRD_GREEN, mortal_rb)
    pygame.draw.rect(screen, BLACK, mortal_rb, 2)
    screen.blit(mortal_rb_text_surface, mortal_rb_text_dest)
    pygame.draw.rect(screen, THIRD_GREEN, god_rb)
    pygame.draw.rect(screen, BLACK, god_rb, 2)
    screen.blit(god_rb_text_surface, god_rb_text_dest)


def draw_start_menu():
    load_background()

    # main box
    pygame.draw.rect(screen, MAIN_GREEN, main_menu_rect)
    pygame.draw.rect(screen, BLACK, main_menu_rect, 2)

    # game title
    screen.blit(title_text_surface, title_text_dest)

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


def draw_stats_screen():
    load_background()

    pygame.draw.rect(screen, MAIN_GREEN, stats_main_box)
    pygame.draw.rect(screen, BLACK, stats_main_box, 2)

    pygame.draw.rect(screen, THIRD_GREEN, back_b)
    pygame.draw.rect(screen, BLACK, back_b, 2)
    screen.blit(back_b_text_surface, back_b_text_dest)

    # pygame.Surface.set_colorkey(user_manual_img, (255, 255, 255))
    screen.blit(user_manual_img, (stats_main_box.left, stats_main_box.top))
