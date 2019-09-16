from socket import *
serverPort=12000
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(("10.124.7.88",serverPort))
print("the server is read to receive ")
while 1:
	sentence,clientAdd=serverSocket.recvfrom(2048)
	File1=open(sentence,"r")
	l=File1.read(2048)
	serverSocket.sendto(bytes(1,"utf-8"),clientAdd)
	print("SENT TO BACK TO CLIENT",1)
	File1.close()
