import pygame
import socket
import pickle

pygame.init()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.235.87', 12345)  # Update the IP address and port as needed
server_socket.bind(server_address)


server_socket.listen(1)

print("Server is listening for connections...")


client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} established.")

server_socket.listen(1)

print("Server is listening for connections...")


client_socket2, client_address2 = server_socket.accept()
print(f"Connection from {client_address2} established.")

window = pygame.display.set_mode((600, 600))
window.fill((255, 255, 255))

circle_radius = 60
color = (0, 0, 255)
color2 = (0,255,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        data = client_socket.recv(1024)
        data = client_socket2.recv(1024)
        circle_pos = pickle.loads(data)
        for position in circle_pos:
            pygame.draw.circle(window, color, position, circle_radius)


        pygame.display.update()


client_socket.close()
client_socket2.close()
server_socket.close()
pygame.quit()