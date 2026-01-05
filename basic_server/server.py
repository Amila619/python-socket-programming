import socket

HOST = "127.0.0.1"
PORT = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
while True:
    conn, addr = server.accept()
    print ("Connection Address is: " , addr)
    conn.send(bytes("Hello!, Welcome to the server!","utf-8"))
