import socket
import threading
import pickle

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_HOST, SERVER_PORT))

def receive():
    while True:
        try:
            message = pickle.loads(client.recv(1024))
            print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        message = input("")
        client.send(pickle.dumps(message))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()


