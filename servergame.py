import socket
import threading
import pickle
import os

ip = os.popen('ipconfig').read()
index = ip.find("IPv4", ip.find("IPv4")+1)
SERVER_HOST = ip[index+36:index+50]
SERVER_PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_HOST, SERVER_PORT))
server.listen()

clients = []


def broadcast(message):
    for client in clients:
        client.send(pickle.dumps(message))


# Inside receive function before starting the thread
def handle(client):
    while True:
        try:
            message = pickle.loads(client.recv(1024))
            broadcast(message)

            # Additional logic to handle troop creation and deployment
            action, data = message
            if action == 'mortal_creation':
                broadcast(('create_mortal', data))
                print("hi")
            elif action == 'mortal_deploy':
                broadcast(('deploy_mortal', data))
                print("hi2")
            elif action == 'god_creation':
                broadcast(('create_god', data))
                print("hi")
            elif action == 'god_deploy':
                broadcast(('deploy_god', data))
                print("hi2")

        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            break


# def handle(client):
    # while True:
        # try:
            # message = pickle.loads(client.recv(1024))
            # broadcast(message)
        # except:
            # index = clients.index(client)
            # clients.remove(client)
            # client.close()
            # break


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        clients.append(client)

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server is running...")
receive()
