# tutorial: https://www.geeksforgeeks.org/pygame-control-sprites/?ref=lbp

import pygame
pygame.init()


class Sprite(pygame.sprite.Sprite):

    # constructor
    def __init__(self, color, height, width):
        super().__init__()
        # inherits from pygame.sprite.Sprite class, so you need to call super().__init__()

        self.height = height
        self.width = width

        self.image = pygame.Surface([width, height])
        self.player_img = pygame.image.load('Tower.png').convert_alpha()
        self.image.blit(self.player_img, self.image.get_rect().x, self.image.get_rect().y)
        self.image.fill(SURFACE_COLOR)
        # any pixels set to the color key will become transparent
        self.image.set_colorkey(COLOR)

        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def move_right(self, pixels):
        self.rect.x += pixels
        if self.rect.x >= WIDTH-self.width:
            self.rect.x = WIDTH-self.width

    def move_left(self, pixels):
        self.rect.x -= pixels
        if self.rect.x <= 0:
            self.rect.x = 0

    def move_forward(self, speed):
        self.rect.y += speed * speed/10
        if self.rect.y >= HEIGHT-self.height:
            self.rect.y = HEIGHT-self.height

    def move_back(self, speed):
        self.rect.y -= speed * speed/10
        if self.rect.y <= 0:
            self.rect.y = 0


# global variables
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 155, 100)
WIDTH = 500
HEIGHT = 500

RED = (255, 0, 0)

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("SPRITES")

all_sprites_list = pygame.sprite.Group()

playerCar = Sprite(RED, 20, 30)
playerCar.rect.x = 200
playerCar.rect.y = 300

all_sprites_list.add(playerCar)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerCar.move_left(10)
    if keys[pygame.K_RIGHT]:
        playerCar.move_right(10)
    if keys[pygame.K_DOWN]:
        playerCar.move_forward(10)
    if keys[pygame.K_UP]:
        playerCar.move_back(10)

    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
