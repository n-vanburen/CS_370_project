import socket
import threading
import pickle
import os

god_count = 0
mortal_count = 0
ip = os.popen('ipconfig').read()
index = ip.find("IPv4", ip.find("IPv4")+1)

SERVER_HOST = ip[index+36: ip.find(" ", index+36)-1]
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
    global god_count
    global mortal_count
    while True:
        try:
            message = pickle.loads(client.recv(1024))

            # Additional logic to handle troop creation and deployment
            action, data = message
            if action == 'mortal_creation':
                broadcast(('create_mortal', data))

            if action == 'mortal_deploy':
                broadcast(('deploy_mortal', data))

            if action == 'god_creation':
                broadcast(('create_god', data))

            if action == 'god_deploy':
                broadcast(('deploy_god', data))

            if action == 'mortal_chosen':
                broadcast(('choose_god', "g"))

            if action == 'god_chosen':
                broadcast(('choose_mortal', "m"))

            if action == 'mortal_heal':
                broadcast(('heal_mortal', "idk"))

            if action == 'god_heal':
                broadcast(('heal_god', "idk"))

            if action == 'press_start':
                if data == 'g':
                    god_count += 1
                if data == 'm':
                    mortal_count += 1
                if mortal_count >= 1 and god_count >= 1:
                    broadcast(('start_game', "epic"))
                    mortal_count = 0
                    god_count = 0

            if action == 'coin_up_god':
                broadcast(('god_up_coin', 'holder'))
            if action == 'coin_up_mortal':
                broadcast(('mortal_up_coin', 'holder'))

            if action == 'god_lightning':
                broadcast(("god_strike", data))
            if action == 'mortal_catapult':
                broadcast(('mortal_strike', data))

        except:
            index = clients.index(client)
            client.close()
            clients.remove(client)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        clients.append(client)

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server is running...")
receive()
