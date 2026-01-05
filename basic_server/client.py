import socket

HOST = "127.0.0.1"
PORT = 1234
BUF_SIZE = 1024

con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con.connect((HOST, PORT))

data = con.recv(BUF_SIZE)
con.close()
print(data.decode("utf-8"))