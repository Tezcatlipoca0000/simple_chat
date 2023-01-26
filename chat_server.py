# Chat app. Code extracted from: 
# https://www.thepythoncode.com/article/make-a-chat-room-application-in-python
#

import socket 
from threading import Thread

# Create a TCP socket
s = socket.socket()

# host and port variables
host = socket.gethostname()
port = 8888

# list of connected clients
clients = set()

#make the port as reusable port
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind the socket to the addrs
s.bind((host, port))

#listen for 2 connections
s.listen(2)
print(f'Server listening in port: {port}')

def listener(cs):
    while True:
        try:
            msg = cs.recv(1024).decode()
        except Exception as e:
            print('Error', e)
            clients.remove(cs)
        else:
            for client in clients:
                client.send(msg.encode())

while True:
    cs, addr = s.accept()
    print('client connected with address: ', addr)

    clients.add(cs)

    t = Thread(target=listener, args=(cs,), daemon=True)
    t.start()

# close clients sockets
for client in clients:
    client.close()

# close server socket
s.close()