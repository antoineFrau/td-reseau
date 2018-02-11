import socket
import json
import time
import datetime
import struct

# get the hostname
host = 'localhost'
port = 3000  # initiate port no above 1024
dataJsonify = {}

TIME1970 = 2208988800L

def timeserver_calculation():
	return datetime.datetime.now().time()
	# t = int(time.time()) + TIME1970
	# t = chr(t>>24&255) + chr(t>>16&255) + chr(t>>8&255) + chr(t&255)
	# return t
	#return time.time()
server_socket = socket.socket()  # get instance
# look closely. The bind() function takes tuple as argument
server_socket.bind((host, port))  # bind host address and port together

# configure how many client the server can listen simultaneously
server_socket.listen(2)
conn, address = server_socket.accept()  # accept new connection
print("Connection from: " + str(address))

while True:
	# receive data stream. it won't accept data packet greater than 1024 bytes
	data = conn.recv(1024).decode()
	if not data:
		# if data is not received break
		break

	dataJsonify = json.loads(data)
	
	title = dataJsonify["title"]
	content = dataJsonify["content"]

	print("from connected user: " + title)
	if title == "giveTime":
		myTime = timeserver_calculation()
		dataToSend = {"title":"TimeFromServ", "content":""+str(myTime)}  # take input
		dataToSend = json.dumps(dataToSend)
		conn.send(dataToSend)

conn.close()  # close the connection


