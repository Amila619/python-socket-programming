import socket
import ssl

host = "www.google.com"
port = 443
BUF_SIZE = 4096

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
context = ssl.create_default_context()
con = context.wrap_socket(sock, server_hostname=host)

con.connect((host, port))

# POST request (Google will reject this)
body = "q=test"
request = (
    "POST / HTTP/1.1\r\n"
    "Host: www.google.com\r\n"
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

print(response.decode(errors="ignore"))

"""
Why Google blocks this

 - Anti-bot protection
 - Requires JavaScript, cookies, TLS fingerprinting
 - POST search is not supported
 - Automated scraping violates their terms
"""