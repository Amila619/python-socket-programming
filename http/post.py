#HTTP using a raw TCP socket
import socket

#We will obtain a simple html file which is available at http://example.com/
#You can check the content by accessing this page in your web browser.

port = 80
address = 'example.com'

BUF_SIZE = 1024

# create a socket object name 'con'
con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con.connect((address, port))

#Try post message as well. 
#Try removing Content-Length-> will give an error message
#Try Putting more than avaialble content length: Nothing will load, since the server wait for more pending content
# This will work with 200 OK

message = "POST / HTTP/1.1\nHost:example.com\nContent-Length:0\nConnection:close\n\n"

con.send(bytes(message,"utf-8"));

#Here, we do not retreive the entire file.
#We are happy with only first part of the file. 

#Task 1:
#It is an exercise for you to retreive entire file as chunks.
#If needed, you can just observe the Content-Length in the Response header, 
#Then retreive the entier file as suited. (Either expand BUF_SIZE or receive and print as chunks)

data = con.recv(BUF_SIZE)
con.close()
print(data.decode("utf-8"))

