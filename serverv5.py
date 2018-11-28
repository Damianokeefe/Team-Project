from socket import socket, AF_INET, SOCK_STREAM
import threading

def broadcast_data(sock, message):
    for socket in CONNECTION_LIST:
        if socket != server and socket != sock:
            try:
                socket.send(message.encode())
            except:
                socket.close()
                CONNECTION_LIST.remove(socket)

CONNECTION_LIST = []
RECV_BUFFER = 4096
PORT = 5000

server = socket(AF_INET, SOCK_STREAM)

def connections():
    while True:
        client, clientAddr = server.accept()
        print("Client [%s:%s] connected" % clientAddr)
        client.send("Type in a username, then press enter to chat.")

def client_connection(client):
    user = client.recv().decode()
    client.send("Welcome to the chat, %s. Type 'quit' to exit." % user)
    broadcast_data("%s has joined." % user)


if __name__ == "__main__":

    server.listen(10)
    CONNECTION_LIST.append(server)
    print("Chat server has started on port: " + str(PORT))