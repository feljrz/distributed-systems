import socket

HOST = '127.0.0.1'
PORT = 5001

# socket.AF_INET -> define a familia (IPv4)
# socket.SOCK_DGRAM -> define o tipo (UDP)
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind((HOST, PORT))
while True:
    msg, client = udp.recvfrom(1024)
    print(f"Server-side: {msg}")
    udp.sendto(msg, client)
