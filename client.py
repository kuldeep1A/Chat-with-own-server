import threading
import socket
from tarfile import ENCODING

nickname = input("Enter the nickname: ")
ENCOD = "ascii"

host = socket.gethostbyname(socket.gethostname())
port = 5050
addr = (host, port)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(__address=addr)

def receive():
    while True:
        try:
            message = client.recv(1024).decode(ENCODING)
            if message == "NICK":
                client.send(nickname.encode(ENCODING))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode(ENCODING))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()