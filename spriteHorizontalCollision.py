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
        self.image.fill(SURFACE_COLOR)

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


def crash():
    global COLLISION
    if (enemyCar.rect.x <= playerCar.rect.x <= enemyCar.rect.x+enemyCar.width
            or enemyCar.rect.x <= playerCar.rect.x+playerCar.width <= enemyCar.rect.x+enemyCar.width):
        COLLISION = True
        print("CRASH")


# global variables
COLOR_2 = (255, 100, 98)
SURFACE_COLOR = (167, 155, 100)
WIDTH = 500
HEIGHT = 500
COLOR_1 = (255, 0, 0)
COLLISION = False

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("SPRITE HORIZONTAL COLLISION")

all_sprites_list = pygame.sprite.Group()

playerCar = Sprite(COLOR_1, 20, 30)
playerCar.rect.x = 0
playerCar.rect.y = 300

enemyCar = Sprite(COLOR_2, 20, 30)
enemyCar.rect.x = WIDTH-enemyCar.width
enemyCar.rect.y = 300

all_sprites_list.add(playerCar)
all_sprites_list.add(enemyCar)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False

    crash()

    if not COLLISION:
        playerMove = 1
        enemyMove = 0.75
    else:
        playerMove = 0
        enemyMove = 0

    # move
    playerCar.move_right(playerMove)
    enemyCar.move_left(enemyMove)

    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
