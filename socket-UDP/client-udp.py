import socket
import time

HOST = '127.0.0.1'
PORT = 5001

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.connect((HOST, PORT))

msg = b"Hello World from client"

while True:
    udp.sendall(msg)
    response = udp.recv(1024)
    print(f"Client-side: {response}")
    time.sleep(3)
    