import socket
import random
import json


host = 'localhost'  # as both code is running on same pc
port = 3000  # socket server port number

client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server

dataToSend = {"title":"giveTime", "content":"bitchplease"}  # take input
fin = 0
while len(dataToSend) >= 2:
	client_socket.send(json.dumps(dataToSend))  # send dataToSend
	data = client_socket.recv(4096).decode()  # receive response

	dataJsonify = json.loads(data)
	
	title = dataJsonify["title"]
	content = dataJsonify["content"]
	if title == "TimeFromServ":
		print "L'heure du serveur est : "+content
	dataToSend = {}

client_socket.close()  # close the connection
