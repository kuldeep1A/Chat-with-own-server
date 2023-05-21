import socket
import threading
# from base64 import encode
from tarfile import ENCODING

port = 5050
ENCODEING = "ascii"
# access the host address by name
host = socket.gethostbyname(socket.gethostname())
addr = (host, port)
# Create a server using socket and add family and type
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)
server.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:

        try:
            message = client.recv(1024)
            broadcast(message)

        except:  # When client disconnects
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            print(f"{nickname} left the chat!".encode(ENCODING))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"Connect with {str(address)}")
        client.send("NICK".encode(ENCODING))
        nickname = client.recv(1024).decode(ENCODING)

        clients.append(client)
        nicknames.append(nickname)

        print(f"Nickname of the client is {nickname}!")
        broadcast(f"{nickname} joined the chat.".encode(ENCODING))
        client.send('Connect to the server!'.encode(ENCODING))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server is listing....")
server_thread = threading.Thread(target=receive)
server_thread.start()
