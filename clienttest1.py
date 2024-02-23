import pygame
import socket
import pickle

pygame.init()


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('192.168.235.87', 12345)
client_socket.connect(server_address)

window = pygame.display.set_mode((600, 600))
window.fill((255, 255, 255))

circle_pos = []
circle_radius = 60
color = (0, 0, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = event.pos
            circle_pos.append(position)

            data = pickle.dumps(circle_pos)
            client_socket.sendall(data)

    pygame.display.update()


client_socket.close()
pygame.quit()