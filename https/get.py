import socket
import ssl

address = "example.com"
port = 443
BUF_SIZE = 1024

# 1. Create a normal TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Create SSL context (recommended way)
context = ssl.create_default_context()

# 3. Wrap the socket with TLS (HTTPS)
con = context.wrap_socket(sock, server_hostname=address)

# 4. Connect to HTTPS server
con.connect((address, port))

# 5. Proper HTTP/1.1 request
message = (
    "GET / HTTP/1.1\r\n"
    "Host: example.com\r\n"
    "Connection: close\r\n"
    "\r\n"
)

con.sendall(message.encode("utf-8"))

# 6. Receive entire response in chunks
response = b""
while True:
    data = con.recv(BUF_SIZE)
    if not data:
        break
    response += data

con.close()

print(response.decode("utf-8", errors="ignore"))
