# tutorial: https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/?ref=lbp
import pygame
pygame.init()

res = (500, 500)
screen = pygame.display.set_mode(res)

white = (255, 255, 255)
light = (170, 170, 170)
dark = (100, 100, 100)

width, height = (screen.get_width(), screen.get_height())

smallFont = pygame.font.SysFont('Corbel', 35)
text = smallFont.render('quit', True, white)

mouse = pygame.mouse.get_pos()

left = width/2-70
top = height/2-20
rect_width = 140
rect_height = 40

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse clicks on the button
            if left <= mouse[0] <= left+rect_width and top <= mouse[1] <= top+rect_height:
                running = False

    screen.fill((60, 25, 60))
    mouse = pygame.mouse.get_pos()

    # mouse hovering over button changes color
    if left <= mouse[0] <= left+rect_width and top <= mouse[1] <= top+rect_height:
        pygame.draw.rect(screen, light, [left, top, rect_width, rect_height])
    else:
        pygame.draw.rect(screen, dark, [left, top, rect_width, rect_height])

    # superimpose text on top of button
    screen.blit(text, (left+50, top))

    pygame.display.update()

pygame.quit()
