import pygame
pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

width = 800
height = 300

# size of block
pixel = 40

screen = pygame.display.set_mode((width, height))

collision = False

playerXPosition = 0
playerYPosition = (height/2)-(pixel/2)

playerXPositionChange = 0

rect = pygame.Rect(playerXPosition, playerYPosition, pixel, pixel)

# define function for setting image at specific coordinates
def playerMove(x, y):
    global rect
    rect = pygame.Rect((x,y), (pixel, pixel))
    pygame.draw.rect(screen, green, rect)

blockXPosition = width-pixel
blockYPosition = (height/2) - (pixel/2)

blockXPositionChange = 0

# function for moving block
def blockMove(x, y):
    pygame.draw.rect(screen, red, [x, y, pixel, pixel])

# collision detection function
def crash():
    global collision
    if (blockXPosition <= playerXPosition <= blockXPosition+pixel
            or blockXPosition <= playerXPosition+pixel <= blockXPosition+pixel):
            collision = True

running = True
while running:
    screen.fill(black)
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    crash()

    if not collision:
        playerXPositionChange = 1
        blockXPositionChange = -0.75
    else:
        playerXPositionChange = 0
        blockXPositionChange = 0

    # move
    playerXPosition += playerXPositionChange
    blockXPosition += blockXPositionChange

    playerMove(playerXPosition, playerYPosition)
    blockMove(blockXPosition, blockYPosition)

    pygame.display.update()

    # test to see if this works
    print(str(rect[0]))

pygame.quit()
