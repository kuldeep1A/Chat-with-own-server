import socket
import threading

port = 5050
# access the host address by name
host = socket.gethostbyname(socket.gethostname())
addr = (host, port)
# Create a server using socket and add family and type
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(__address=addr)

def handle(client):
    while True:
        try:
            message = client.

def receive():
    while True:
        client, address = server.accept()
        print()
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listing....")
server_thread = threading.Thread(target=receive)
server_thread.start()
