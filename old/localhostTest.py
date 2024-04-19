import socket
import threading

SERVER_HOST = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_HOST, SERVER_PORT))
server.listen()

clients = []


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        clients.append(client)

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server is running...", SERVER_HOST)
receive()
