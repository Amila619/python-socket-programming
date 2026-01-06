import socket
import ssl

host = "httpbin.org"
port = 443
BUF_SIZE = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
context = ssl.create_default_context()
con = context.wrap_socket(sock, server_hostname=host)

con.connect((host, port))

body = "name=student&topic=http"

request = (
    "POST /post HTTP/1.1\r\n"
    "Host: httpbin.org\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    f"Content-Length: {len(body)}\r\n"
    "Connection: close\r\n"
    "\r\n"
    + body
)

con.sendall(request.encode())

response = b""
while True:
    data = con.recv(BUF_SIZE)
    if not data:
        break
    response += data

con.close()

print(response.decode())
