# tutorial: https://www.geeksforgeeks.org/collision-detection-in-pygame/?ref=lbp
import pygame
import random
pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

width = 650
height = 700

# size of block
pixel = 64

screen = pygame.display.set_mode((width, height))

playerXPosition = (width/2)-(pixel/2)
playerYPosition = height-pixel-10

playerXPositionChange = 0

# define function for setting image at specific coordinates
def playerMove(x, y):
    pygame.draw.rect(screen, green, [(x, y), (pixel, pixel)])

blockXPosition = random.randint(0, (width-pixel))
blockYPosition = 0 - pixel

blockXPositionChange = 0
blockYPositionChange = 2

# function for moving block
def blockMove(x, y):
    pygame.draw.rect(screen, red, [x, y, pixel, pixel])

# collision detection functino
def crash():
    global blockYPosition

    # checks that block has entered the same horizontal space as player
    if playerYPosition < (blockYPosition+pixel):

        # checks that player in under block
        if ((blockXPosition <= playerXPosition <= (blockXPosition + pixel))
        or (blockXPosition <= (playerXPosition + pixel) <= (blockXPosition + pixel))):
            blockYPosition = height + 1000
            print('CRASH')


running = True
while running:
    screen.fill(black)
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerXPositionChange = 1
            if event.key == pygame.K_LEFT:
                playerXPositionChange = -1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                playerXPositionChange = 0

    # bound the player to the screen
    if playerXPosition >= width-pixel:
        playerXPosition = (width-pixel)
    if playerXPosition <= 0:
        playerXPosition = 0

    # allow block to loop back to top if no collision
    if (blockYPosition >= height and blockXPosition <= (height+200)):
        blockYPosition = 0-pixel
        blockXPosition = random.randint(0, (width-pixel))

    # move
    playerXPosition += playerXPositionChange
    blockYPosition += blockYPositionChange
    playerMove(playerXPosition, playerYPosition)
    blockMove(blockXPosition, blockYPosition)
    crash()

    pygame.display.update()

pygame.quit()
