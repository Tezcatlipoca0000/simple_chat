# Chat app. Code extracted from: 
# https://www.thepythoncode.com/article/make-a-chat-room-application-in-python
#

import socket
from threading import Thread

s = socket.socket()

# host and port
host = socket.gethostname()
port = 8888

print('connecting... ')
s.connect((host, port))
print('Connected! ')

name = input("Enter your name: ")

def listener():
    while True:
        msg = s.recv(1024).decode()
        print("\n" + msg)

t = Thread(target=listener, daemon=True)
t.start()

while True:
    send = input()
    if send.lower() == 'q':
        break
    send = f"{name} : {send}"
    s.send(send.encode())

s.close()