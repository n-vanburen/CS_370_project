import pygame
import socket
import pickle
import threading

pygame.init()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.235.87', 12345)  # Update the IP address and port as needed
server_socket.bind(server_address)

server_socket.listen(2)  # Allowing up to 2 clients to connect

print("Server is listening for connections...")

clients = []

def handle_client(client_socket, client_index):
    while True:
        data = client_socket.recv(1024)
        circle_pos = pickle.loads(data)
        for position in circle_pos:
            pygame.draw.circle(window, colors[client_index], position, circle_radius)
        pygame.display.update()

try:
    for i in range(2):
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} established.")
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket, i)).start()

    window = pygame.display.set_mode((600, 600))
    window.fill((255, 255, 255))

    circle_radius = 60
    colors = [(0, 0, 255), (0, 255, 0)]  # Different colors for each client

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

except Exception as e:
    print("An error occurred:", e)

finally:
    for client_socket in clients:
        client_socket.close()
    server_socket.close()
    pygame.quit()