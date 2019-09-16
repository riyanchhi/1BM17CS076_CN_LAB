from socket import *
clientName="10.124.7.88"
clientPort=12000
ClientSocket=socket(AF_INET,SOCK_STREAM)
ClientSocket.connect((clientName,clientPort))
sentence=input("enter file name")
ClientSocket.send(sentence.encode())
Filec=ClientSocket.recv(1024).decode()
print('from Server',Filec)
ClientSocket.close()


