import pygame
import random
import socket
import threading


def handle_client(client_socket, addr):
    try:
        while True:
            # receive and print client messages
            request = client_socket.recv(1024).decode("utf-8")
            if request.lower() == "close":
                client_socket.send("closed".encode("utf-8"))
                break
            print(f"Received: {request}")
            # convert and send accept response to the client
            response = "accepted"
            client_socket.send(response.encode("utf-8"))
    except Exception as e:
        print(f"Error when hanlding client: {e}")
    finally:
        client_socket.close()
        print(f"Connection to client ({addr[0]}:{addr[1]}) closed")


def run_server():
    server_ip = "127.0.0.1"  # server hostname or IP address
    port = 8000  # server port number
    # create a socket object
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # bind the socket to the host and port
        server.bind((server_ip, port))
        # listen for incoming connections
        server.listen()
        print(f"Listening on {server_ip}:{port}")

        while True:
            # accept a client connection
            client_socket, addr = server.accept()
            print(f"Accepted connection from {addr[0]}:{addr[1]}")
            # start a new thread to handle the client
            thread = threading.Thread(target=handle_client, args=(client_socket, addr,))
            thread.start()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.close()


run_server()

pygame.init()

width = 700
height = 550

blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode((width, height))

# ball variables
ball_X = width/2-12
ball_Y = height/2-12
ball_XChange = 1 * random.choice((1, -1))
ball_YChange = 1
ballPixel = 12

# smaller boundary - rectangle variables
rect_left = width/4
rect_top = height/4
rect_width = width/2
rect_height = height/2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if ball_X+ballPixel >= rect_width+rect_left or ball_X-ballPixel <= rect_left:
        ball_XChange *= -1
    if ball_Y+ballPixel >= rect_height+rect_top or ball_Y-ballPixel <= rect_top:
        ball_YChange *= -1

    ball_X += ball_XChange
    ball_Y += ball_YChange

    pygame.time.delay(10)

    screen.fill(black)

    ball = pygame.draw.circle(screen, blue, (ball_X, ball_Y), 12)
    boundary_rect = pygame.draw.rect(screen, white, [rect_left, rect_top, rect_width, rect_height], 2)

    pygame.display.update()

pygame.quit()