import socket
adr=socket.gethostbyname(socket.gethostname())
print adr
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)#creates socket

port = 12010 #define a port number on which the server listens for incoming connections.
serverSocket.bind((adr, port)) #Binds the ip address to the port.
serverSocket.listen(1) #Starts lisening to the incoming connection on the port number defined earlier.

while True:
	print 'Ready to serve...'
	connectionSocket, addr = serverSocket.accept() #Accepts the clinet connection.
	try:
                message = connectionSocket.recv(1024) #receives message from client
                filename = message.split()[1]
                f = open(filename[1:]) #opens the requested html file.
                outputdata=f.read() #read all the contents of the html file and stores in 'outputdata' variable.
                connectionSocket.send("HTTP/1.1 200 OK\nServer: webServer.py\nContent-Type: text/html; charset=UTF-8\n") #sends a 200 OK header line
                connectionSocket.send(outputdata) #Sends the output data through the connection to client.
                connectionSocket.close() 
	except IOError:
		connectionSocket.send("\n404 File Not Found\n") #Sends an 404 error message to the client.
		connectionSocket.close() #closes the client connecton.
serverSocket.close() #closes the server socket
