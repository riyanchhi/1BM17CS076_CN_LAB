from socket import *
ServerName="10.124.7.89"
Serverport=12000
clientsocket=socket(AF_INET,SOCK_DGRAM)
sentence=input("enter file name")
clientsocket.sendto(bytes(sentence,"utf-8"),(ServerName,Serverport))
filec,serverAddress=clientsocket.recvfrom(2048)
print("from server:",filec)
clientsocket.close()
