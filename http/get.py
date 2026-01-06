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

#HTTP GET request is specific:
#1. One space between GET and path, and another one space between path and version
#2. \n newline at the end of first line.
#3. Additional headers in subsequent lines.
#4. The end of message must be marked with two newline characters 
#Additional headers can be included. (You can find some options using your browsers Network Monitor tool)
message = "GET / HTTP/1.1\nHost:example.com\nConnection:close\n\n"

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

#Expected output: HTTP/1.1 200 OK with additional headers, 
#Followed by \n\n (Two new lines to mark the end of the header, and then the content)
#Content is an html file which begin with "<!doctype html>"

#Task 2:
#Verify / is the same path as /index.html by changing the path

#Task 3: 
#Try receiving non existant file. like /obviously-nonexistant instead of /
#You should receive HTTP/1.1 404 Not Found

#Task 4: 
#Try changing the HTTP version to 2 instead of 1.1
#You might receive HTTP/1.0 505 HTTP Version Not Supported
#This means server is old-style. More modern servers support version 2 which has lot of additional features.