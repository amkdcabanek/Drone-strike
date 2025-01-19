import socket
import threading
import pygame
import pickle

HEADER = 64
PORT = 5050
SERVER = "26.203.108.55"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"Connected by: {addr}")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            unpickle = pickle.loads(msg)
            print(f"[{addr}] {unpickle}")
            conn.send("Msg recieved".encode(FORMAT))

    conn.close()



def start():
    server.listen()
    print(f"Listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNETIONS] {threading.active_count() - 1}")


print("starting server...")
start()

