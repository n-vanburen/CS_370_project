import socket
import threading
import pickle

SERVER_HOST = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_HOST, SERVER_PORT))
server.listen()

clients = []


def broadcast(message):
    for client in clients:
        client.send(pickle.dumps(message))


def handle(client):
    while True:
        try:
            message = pickle.loads(client.recv(1024))
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        clients.append(client)

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server is running...")
print("Server IP: " + SERVER_HOST)
receive()
