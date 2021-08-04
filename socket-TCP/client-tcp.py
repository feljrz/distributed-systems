import socket
import time

HOST = '127.0.0.1'
PORT = 5001

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((HOST, PORT))

msg = b"Hello World from client"

while True:
    tcp.sendall(msg)
    response = tcp.recv(1024)
    print(f"Client-side: {response}")
    time.sleep(3)



