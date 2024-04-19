import pygame
import sys

#Initialize Pygame
pygame.init()

#Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Timer Example")

#Load your background image
background_image = pygame.image.load("../assets/Background.png")  # Change "background.jpg" to your image file path

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Fonts
font = pygame.font.SysFont("Font.tff", 36)

#Game variables
start_time = pygame.time.get_ticks()  # Get the starting time of the game
game_duration = 5 * 60 * 1000  # 5 minutes in milliseconds

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)  # Fill the screen with white

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Calculate elapsed time
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time

    # Convert milliseconds to minutes and seconds
    minutes = (game_duration - elapsed_time) // 60000
    seconds = ((game_duration - elapsed_time) // 1000) % 60

    # Check if the game is over
    if elapsed_time >= game_duration:
        running = False

    # Render the timer text
    timer_text = f"Time Left: {minutes:02}:{seconds:02}"
    timer_surface = font.render(timer_text, True, BLACK)
    screen.blit(timer_surface, (20, 20))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    # clock.tick(60)

#Game over
game_over_text = font.render("Time's up! Game Over!", True, BLACK)
game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(game_over_text, game_over_rect)
pygame.display.flip()

#Wait for a few seconds before quitting
pygame.time.wait(3000)
pygame.quit()
sys.exit()