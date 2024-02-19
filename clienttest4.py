import pygame
import socket
import pickle

pygame.init()

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = ('192.168.235.87', 12345)  # Update the IP address and port as needed
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

            # Serialize circle_pos
            data = pickle.dumps(circle_pos)

            # Send data size to server
            client_socket.sendall(str(len(data)).encode())

            # Send serialized data to server
            client_socket.sendall(data)

    # Receive data size from server
    data_size = client_socket.recv(1024)
    data_size = int(data_size.decode())

    # Receive data from server based on data size
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
pygame.quit()
