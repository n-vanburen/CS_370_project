from threading import Thread
from socketserver import ThreadingMixIn
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("Hello World!", "utf-8"))

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True

def serve_on_port(port):
    server = ThreadingHTTPServer(("localhost",port), Handler)
    server.serve_forever()

Thread(target=serve_on_port, args=[1111]).start()
serve_on_port(2222)

import socket
import sys


# specify Host and Port
# HOST = ''
# PORT = 5789

# soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# try:
    # With the help of bind() function
    # binding host and port
    # soc.bind((HOST, PORT))

# except socket.error as message:

    # if any error occurs then with the
    # help of sys.exit() exit from the program
    # print('Bind failed. Error Code : '
          # + str(message[0]) + ' Message '
          # + message[1])
    # sys.exit()

# print if Socket binding operation completed
# print('Socket binding operation completed')

# With the help of listening () function
# starts listening
# soc.listen(9)

# conn, address = soc.accept()
# print the address of connection
# print('Connected with ' + address[0] + ':'
      # + str(address[1]))