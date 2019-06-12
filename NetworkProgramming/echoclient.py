import socket
import time


host='127.0.0.1'
port=4467
try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print('The socket was created ...sucessfully')
except socket.error as err:
	print('socket was not created due to the error %s'%err)

s.connect((host,port))

while True:
	
	data=input(">>>")
	
	data=data.encode()
	s.send(data)
	print('recived data',s.recv(1024))
s.close()

