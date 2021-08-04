import socket

HOST = '127.0.0.1'
PORT = 5001

# socket.AF_INET -> define a familia (IPv4)
# socket.SOCK_STREAM -> define o tipo (TCP)
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((HOST, PORT))
tcp.listen()
while True:
    conn, client = tcp.accept()
    print(client)
    while True:
        msg = conn.recv(1024) #bloco
        if not msg:
            break
        print(f"Server-side: {msg}")
        conn.sendall(msg)
    conn.close()



