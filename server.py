import socket

s = ('localhost' , 12347)

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

server.bind(s)

server.listen(2)

con , addr = server.accept()

while True:
	send_data = raw_input(">> ")
	con.send(send_data)