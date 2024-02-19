import pygame
import socket
import pickle

pygame.init()

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_address = ('192.168.235.87', 12345)  # Update the IP address and port as needed
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print("Server is listening for connections...")

# Accept incoming connection
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} established.")

window = pygame.display.set_mode((600, 600))
window.fill((255, 255, 255))

circle_radius = 60
color = (0, 0, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Receive data size from client
    data_size = client_socket.recv(500000)
    data_size = int(data_size.decode())

    # Receive data from client based on data size
    received_data = b""
    while len(received_data) < data_size:
        packet = client_socket.recv(data_size - len(received_data))
        if not packet:
            break
        received_data += packet

    # Deserialize received data
    circle_pos = pickle.loads(received_data)

    # Draw circles based on received positions
    for position in circle_pos:
        pygame.draw.circle(window, color, position, circle_radius)

    pygame.display.update()

# Clean up the connection
client_socket.close()
server_socket.close()
pygame.quit()
