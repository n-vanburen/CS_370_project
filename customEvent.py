# from tutorial: https://www.geeksforgeeks.org/how-to-add-custom-events-in-pygame/?ref=lbp

import pygame
pygame.init()

# program will inflate/deflate a rect when cursor is over it and change the bg color every .5sec

screen = pygame.display.set_mode((500, 500))
timer = pygame.time.Clock()

pygame.display.set_caption('Custom Events')

# colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# track active color
bg_active_color = WHITE
screen.fill(WHITE)

# custom event to change color
CHANGE_COLOR = pygame.USEREVENT + 1
# custom event to inflate/deflate rectangle
ON_BOX = pygame.USEREVENT + 2

# create rectangle
box = pygame.Rect((255, 255, 50, 50))
grow = True

# post even to switch colors using timer method
pygame.time.set_timer(CHANGE_COLOR, 500)

running = True
while running:
    for event in pygame.event.get():
        if event.type == CHANGE_COLOR:
            if bg_active_color == GREEN:
                screen.fill(GREEN)
                bg_active_color = WHITE
            elif bg_active_color == WHITE:
                screen.fill(WHITE)
                bg_active_color = GREEN

        if event.type == ON_BOX:
            if grow:
                box.inflate_ip(3, 3)
                grow = box.width < 75
            else:
                box.inflate_ip(-3, -3)
                grow = box.width < 50

        if event.type == pygame.QUIT:
            running = False

    # post event when cursor is over box
    if box.collidepoint(pygame.mouse.get_pos()):
        pygame.event.post(pygame.event.Event(ON_BOX))

    # draw the rectange to the screen
    pygame.draw.rect(screen, RED, box)

    # update screen
    pygame.display.update()

    # set frames per second
    timer.tick(30)

pygame.quit()