#import socket
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

def connections():
    while True:
        conn, addr = server.accept()
        print("Client [%s:%s] connected" % addr)
        conn.send(("Type in a username, then press enter to chat.").encode())
        addresses[conn] = addr
        Thread(target=client_connection, args=(conn,)).start()

def client_connection(conn):
    reply = conn.recv(1024)
    user = reply.decode()
    conn.send(("Welcome to the chat, %s." % user).encode())
    welcome = "%s has joined." % user
    broadcast(welcome.encode())
    clients[conn] = user

    while True:
        message = conn.recv(1024)
        message = message.decode()
        if message != "{quit}":
            broadcast(message, user + ": ")
        else:
            conn.send(("{quit}").encode())
            conn.close()
            del clients[conn]
            broadcast(("%s has left the chat." % user).encode())
            break

def broadcast(message, pre=""):
    for sock in clients:
        msgSend = pre + message
        sock.send((msgSend).encode())

clients = {}
addresses = {}

HOST = ''
PORT = 5000
ADDR = (HOST,PORT)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDR)

if __name__ == "__main__":

    server.listen(10)
    print("Chat server has started on port: " + str(PORT))
    ACCEPT_THREAD = Thread(target=connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    server.close()