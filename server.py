import socket
import threading

port = 5050
# access the host address by name
host = socket.gethostbyname(socket.gethostname())
# Create a server using socket and add family and stream
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

