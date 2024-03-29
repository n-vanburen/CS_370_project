import pygame
# import pygame
# import pygame.display

# import gameBoard
# from gameBoard import *
import StateMachine
# pygame.init()  # need this for font
# commented out is already included in gameBoard

font = pygame.font.Font(None, 20)


class Fighter(pygame.sprite.Sprite):
    height = 50
    width = 50
    moving = True
    crash = False
    hit_right_barrier = False
    hit_left_barrier = False
    first_hit = True
    text_surface = font.render("text", True, (0, 0, 0))
    attack_time_counter = 0
    spawn_time = 0

    # constructor
    def __init__(self, color, health, attack_strength, speed, cost, team, attack_speed, photo):
        super().__init__()
        # inherits from pygame.sprite.Sprite class, so you need to call super().__init__()

        self.health = health
        self.attack_strength = attack_strength
        self.speed = speed
        self.cost = cost
        self.team = team
        self.attack_speed = attack_speed
        self.color = color
        self.photo = photo

        self.image = pygame.Surface([self.width, self.height])
        """if Sorceress or Cyclops:
            self.image = pygame.transform.flip(pygame.image.load(self.photo).convert_alpha(),True, False)
        else:
            self.image = pygame.image.load(self.photo).convert_alpha()"""
        self.image = pygame.transform.scale(self.photo, (75, 75))
        self.rect = self.image.get_rect()

        # pygame.draw.rect(self.image, color, pygame.Rect(0, 0, self.width, self.height))
        # self.rect = self.image.get_rect()

        # self.text_surface = font.render(str(self.health), True, (0, 0, 0))
        # self.image.blit(self.text_surface, (self.rect.x+5, self.rect.y+5))
        self.update_health_label()

    def move_right(self, pixels):
        self.rect.x += pixels
        if self.rect.x >= StateMachine.right_barrier_coord-self.width:
            self.rect.x = StateMachine.right_barrier_coord-self.width
            self.hit_right_barrier = True
        else:
            self.hit_right_barrier = False

    def move_left(self, pixels):
        self.rect.x -= pixels
        if self.rect.x <= StateMachine.left_barrier_coord:
            self.rect.x = StateMachine.left_barrier_coord
            self.hit_left_barrier = True
        else:
            self.hit_left_barrier = False

    def update_health_label(self):
        # text_surface = font.render(input_text, True, (255, 255, 255))
        # screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        self.text_surface = font.render(str(self.health), True, (150, 150, 150))
        # screen.blit(self.text_surface, (self.rect.x+self.rect.width+10, self.rect.y+self.rect.height+10))
        StateMachine.screen.blit(self.text_surface, (self.rect.x+5, self.rect.y+5))


class FootSoldier(Fighter):
    health = 20
    attack_strength = 5
    speed = 1
    cost = 50
    team = 'm'
    color = (255, 255, 255)
    attack_speed = 5000
    photo = pygame.image.load("heroknight_attack1_0.png").convert_alpha()

    def __init__(self):
        super().__init__(self.color, self.health, self.attack_strength, self.speed, self.cost,
                         self.team, self.attack_speed, self.photo)


class Minion(Fighter):
    health = 20
    attack_strength = 5
    speed = 1
    cost = 50
    team = 'g'
    color = (73, 52, 33)
    attack_speed = 5000
    photo = pygame.transform.flip(pygame.image.load("Minotaur.png").convert_alpha(), True, False)

    def __init__(self):
        super().__init__(self.color, self.health, self.attack_strength, self.speed, self.cost,
                         self.team, self.attack_speed, self.photo)


class Eagle(Fighter):
    health = 20
    attack_strength = 15
    speed = 1.4
    cost = 75
    team = 'm'
    color = (21, 92, 240)
    attack_speed = 4000
    photo = pygame.transform.flip(pygame.image.load("eagle.png").convert_alpha(), True, False)

    def __init__(self):
        super().__init__(self.color, self.health, self.attack_strength, self.speed, self.cost,
                         self.team, self.attack_speed, self.photo)


class Harpy(Fighter):
    health = 20
    attack_strength = 15
    speed = 1.4
    cost = 75
    team = 'g'
    color = (63, 76, 20)
    attack_speed = 4000
    photo = pygame.image.load("harpy.png").convert_alpha()

    def __init__(self):
        super().__init__(self.color, self.health, self.attack_strength, self.speed, self.cost,
                         self.team, self.attack_speed, self.photo)


class Archer(Fighter):
    health = 10
    attack_strength = 0
    speed = 0
    cost = 100
    team = 'm'
    color = (45, 90, 55)
    attack_speed = 10000
    photo = pygame.image.load("preview.png").convert_alpha()

    def __init__(self):
        super().__init__(self.color, self.health, self.attack_strength, self.speed, self.cost,
                         self.team, self.attack_speed, self.photo)


class Sorceress(Fighter):
    health = 10
    attack_strength = 10
    speed = 0
    cost = 100
    team = 'g'
    color = (20, 21, 22)
    attack_speed = 10000
    photo = pygame.transform.flip(pygame.image.load("b_witch_idle.png").convert_alpha(), True, False)

    def __init__(self):
        super().__init__(self.color, self.health, self.attack_strength, self.speed, self.cost,
                         self.team, self.attack_speed, self.photo)


class Cavalry(Fighter):
    health = 30
    attack_strength = 15
    speed = 1.8
    cost = 125
    team = 'm'
    color = (40, 80, 120)
    attack_speed = 3000
    photo = pygame.image.load("cavalry.jpg").convert_alpha()

    def __init__(self):
        super().__init__(self.color, self.health, self.attack_strength, self.speed, self.cost,
                         self.team, self.attack_speed, self.photo)


class Hellhound(Fighter):
    health = 30
    attack_strength = 15
    speed = 1.8
    cost = 125
    team = 'g'
    color = (200, 70, 90)
    attack_speed = 3000
    photo = pygame.image.load("hellhouns.jpg").convert_alpha()

    def __init__(self):
        super().__init__(self.color, self.health, self.attack_strength, self.speed, self.cost,
                         self.team, self.attack_speed, self.photo)


class TrojanHorse(Fighter):
    health = 50
    attack_strength = 20
    speed = 0.6
    cost = 200
    team = 'm'
    color = (60, 72, 32)
    attack_speed = 8000
    photo = pygame.image.load("horse.png").convert_alpha()

    def __init__(self):
        super().__init__(self.color, self.health, self.attack_strength, self.speed, self.cost,
                         self.team, self.attack_speed, self.photo)


class Cyclops(Fighter):
    health = 50
    attack_strength = 20
    speed = 0.6
    cost = 200
    team = 'g'
    color = (5, 50, 100)
    attack_speed = 8000
    photo = pygame.transform.flip(pygame.image.load("Cyclops.png").convert_alpha(), True, False)

    def __init__(self):
        super().__init__(self.color, self.health, self.attack_strength, self.speed, self.cost,
                         self.team, self.attack_speed, self.photo)


class Achilles(Fighter):
    health = 40
    attack_strength = 25
    speed = 1.4
    cost = 300
    team = 'm'
    color = (20, 200, 100)
    attack_speed = 6000
    photo = pygame.image.load("achilles.jpg").convert_alpha()

    def __init__(self):
        super().__init__(self.color, self.health, self.attack_strength, self.speed, self.cost,
                         self.team, self.attack_speed, self.photo)


class Medusa(Fighter):
    health = 40
    attack_strength = 25
    speed = 1.4
    cost = 300
    team = 'g'
    color = (70, 30, 20)
    attack_speed = 6000
    photo = pygame.image.load("medusa.jpg").convert_alpha()

    def __init__(self):
        super().__init__(self.color, self.health, self.attack_strength, self.speed, self.cost,
                         self.team, self.attack_speed, self.photo)


class Arrow(pygame.sprite.Sprite):
    height = 10
    width = 25
    halfway = False  # the archers only have a range of half the battlefield
    team = 'm'
    attack_strength = 5
    speed = 0.6
    color = StateMachine.BLACK
    crash = False

    # constructor
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Static.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        # self.image = pygame.Surface([self.width, self.height])
        # pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width, self.height))
        self.rect = self.image.get_rect()

    def move_right(self, pixels):
        self.rect.x += pixels
        if self.rect.x+self.width >= StateMachine.screen_w/2:
            self.halfway = True
        else:
            self.halfway = False


class Spell(pygame.sprite.Sprite):
    height = 10
    width = 25
    halfway = False  # the archers only have a range of half the battlefield
    team = 'g'
    attack_strength = 5
    speed = 0.6
    color = StateMachine.WHITE
    crash = False

    # constructor
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([self.width, self.height])
        pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width, self.height))
        self.rect = self.image.get_rect()

    def move_left(self, pixels):
        self.rect.x -= pixels
        if self.rect.x <= StateMachine.screen_w/2:
            self.halfway = True
        else:
            self.halfway = False
