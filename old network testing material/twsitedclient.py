from twisted.internet import reactor, protocol
import pygame
import sys

class ClientProtocol(protocol.Protocol):
    def connectionMade(self):
        print("Connection established")

    def dataReceived(self, data):
        pass

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Client Window')

# Start the Twisted reactor
reactor.connectTCP("localhost", 9999, protocol.ClientFactory())
reactor.run()

# Game loop for drawing circles and sending data to the server
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Send circle position data to the server when mouse button is pressed
            x, y = event.pos
            position_data = f"{x},{y}"
            client_protocol.transport.write(position_data.encode())
            pygame.draw.circle(window, (0, 0, 255), (x, y), 30)
            pygame.display.update()

pygame.quit()
sys.exit()
