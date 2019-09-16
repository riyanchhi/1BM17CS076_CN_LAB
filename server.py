from socket import *
servername="10.124.7.88"
serverPort=12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind((servername,serverPort))
serverSocket.listen(1)
print("the server is ready to recieve")
while 1:
	connectionSocket,addr=serverSocket.accept()
	sentence=connectionSocket.recv(1024).decode()
	File=open(sentence,"r")
	l=File.read(1024)
	connectionSocket.send(l.encode())	
	File.close()
	connectionSocket.close()

