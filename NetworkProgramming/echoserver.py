import socket
import time
try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print('socket sucessfully created........')
except socket.error as err:
	print('socket is not created due to the error %s'%err)

port=4467
host='127.0.0.1'
s.bind((host,port))

s.listen(5)
c,addr=s.accept()
print("got connection from ",addr)

while True:
	
	
	data_recv=c.recv(1024)
	print('data received',data_recv)
	val=input(">>>")
	val=val.upper()
	c.send(val.encode())
	
c.close()