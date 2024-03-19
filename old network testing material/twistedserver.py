from twisted.internet import reactor, protocol
import pygame

class ServerProtocol(protocol.Protocol):
    def dataReceived(self, data):
        # Decode the received data
        position = data.decode().strip().split(',')
        x, y = map(int, position)

        # Draw the circle on the server's window
        pygame.draw.circle(window, (255, 0, 0), (x, y), 30)
        pygame.display.update()

class ServerFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return ServerProtocol()

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((600, 600))
window.fill((255, 255, 255))
pygame.display.set_caption('Server Window')

# Start the Twisted reactor
reactor.listenTCP(9999, ServerFactory())
reactor.run()