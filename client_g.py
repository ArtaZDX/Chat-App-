import socket

client = socket.socket()

client.connect(('localhost' , 20037))

while True:
	data_get = client.recv(100)
	print(data_get)