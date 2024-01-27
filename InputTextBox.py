# from tutorial: https://www.geeksforgeeks.org/pygame-working-with-text/?ref=lbp

import pygame
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 500))

# add font style and size
font = pygame.font.Font(None, 40)

input_text = ''
other_text = 'Welcome!'

# set left, top, width, height of rect for input box
input_rect = pygame.Rect(200, 200, 140, 32)

# colors to depict whether cursor is actively in box or not
active_color = (173, 216, 230)
passive_color = (211, 211, 211)
current_color = passive_color
active = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # when mouse collides with rectangle, active
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:

                # store current text minus last char
                input_text = input_text[:-1]

            else:
                input_text += event.unicode

    screen.fill((0, 0, 0))

    if active:
        current_color = active_color
    else:
        current_color = passive_color

    pygame.draw.rect(screen, current_color, input_rect)

    # render the input text
    text_surface = font.render(input_text, True, (255, 255, 255))
    # put the text in the rectangle (+5, so it's not right on the edge of the rect)
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    # if text is longer than rect, make it wider, minimum size of 100
    input_rect.w = max(100, text_surface.get_width() + 10)

    other_txt_surface = font.render(other_text, True, (128, 128, 128))
    text_rect = other_txt_surface.get_rect()
    text_rect.center = (100, 100)
    screen.blit(other_txt_surface, text_rect)

    # update screen
    pygame.display.flip()

    # 60 fps
    clock.tick(60)


pygame.quit()
