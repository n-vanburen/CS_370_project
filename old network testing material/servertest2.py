import pygame
import socket
import pickle
import threading

pygame.init()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.235.87', 12345)  # Update with your server's IP address and port
server_socket.bind(server_address)

server_socket.listen(2)  # Allowing up to 2 clients to connect

print("Server is listening for connections...")

clients = []
lock = threading.Lock()

def handle_client(client_socket, client_index):
    while True:
        data = client_socket.recv(1024)
        circle_pos = pickle.loads(data)
        with lock:
            for position in circle_pos:
                pygame.draw.circle(window, colors[client_index], position, circle_radius)
        pygame.display.update()
        send_circles_to_clients()

def send_circles_to_clients():
    circles_data = pickle.dumps(circle_positions)
    for client_socket in clients:
        client_socket.send(circles_data)

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
    circle_positions = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mouse_state = pygame.mouse.get_pressed()
        if mouse_state[0]:  # Left mouse button clicked
            mouse_position = pygame.mouse.get_pos()
            with lock:
                circle_positions.append(mouse_position)
            pygame.draw.circle(window, colors[0], mouse_position, circle_radius)
            pygame.display.update()
            send_circles_to_clients()

except Exception as e:
    print("An error occurred:", e)

finally:
    for client_socket in clients:
        client_socket.close()
    server_socket.close()
    pygame.quit()