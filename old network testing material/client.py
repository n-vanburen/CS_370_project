import pygame
import socket
import pickle
import threading

pygame.init()

server_address = ('192.168.235.87', 12345)  # Update with the server's IP address and port

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

window = pygame.display.set_mode((600, 600))
window.fill((255, 255, 255))

def receive_data():
    global window
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            circle_pos = pickle.loads(data)
            for position in circle_pos:
                pygame.draw.circle(window, (0, 255, 0), position, 30)
            pygame.display.update()
        except Exception as e:
            print("Error:", e)
            break

threading.Thread(target=receive_data).start()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event.pos
                data = pickle.dumps([mouse_pos])
                client_socket.send(data)

client_socket.close()
pygame.quit()
