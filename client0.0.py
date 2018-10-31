import socket, select, string, sys

def prompt():
    sys.stdout.write('<You>: ')
    sys.stdout.flush()

def recieve():
    sys.stdout.write('<Server>: ')
    #sys.stdout.flush()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage : python client0.0.py hostname port")

    host = 'localhost' #sys.argv[1]
    port = 5000 #int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    try:
        s.connect((host, port))
    except:
        print("Unable to connect to server")
        sys.exit()

    print("Connected to server, start typing")
    prompt()

    while 1:
        socket_list = [sys.stdin, s]

        read_sockets, write_sokcets, error_sockets = select.select(socket_list, [], [])

        for sock in read_sockets:
            if sock == s:
                data = sock.recv(4096)
                if not data:
                    print("\n Disconnected from server")
                    sys.exit()
                else:
                    sys.stdout.write(data.decode())
                    prompt()

            else:
                msg = sys.stdin.readline()
                s.send(msg.encode())
                recieve()