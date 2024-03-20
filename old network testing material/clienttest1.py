
import pygame
import socket
import pickle

pygame.init()

server_address = ('192.168.235.87', 12345)  # Update with the server's IP address and port

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

window = pygame.display.set_mode((600, 600))
window.fill((255, 255, 255))

circle_radius = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button clicked
                mouse_position = pygame.mouse.get_pos()
                circle_pos = [mouse_position]
                data = pickle.dumps(circle_pos)
                client_socket.send(data)

    pygame.display.update()

client_socket.close()
pygame.quit()