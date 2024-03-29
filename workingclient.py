import pygame
import socket
import threading
import pickle

SERVER_HOST = input("what is the IP of the server")
SERVER_PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_HOST, SERVER_PORT))

pygame.init()

window = pygame.display.set_mode((600, 600))
window.fill((255, 255, 255))

circle_radius = 60
color = (0, 255, 0)

def receive():
    while True:
        try:
            message = pickle.loads(client.recv(1024))
            draw_circle(message)
        except:
            print("An error occurred!")
            client.close()
            break

def draw_circle(position):
    pygame.draw.circle(window, color, position, circle_radius)
    pygame.display.update()

def send_position(position):
    client.send(pickle.dumps(position))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = event.pos
            send_position(position)

pygame.quit()
client.close()
