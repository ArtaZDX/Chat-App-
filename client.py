import socket

c = ('localhost' , 12347)

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

client.connect(c)

while True:
	data = client.recv(1024)
	print(data)