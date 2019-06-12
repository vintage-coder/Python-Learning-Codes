import socket

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
except socket.error as err:
	print("socket was not created due to the error %s"%err)

host='127.0.0.1'
port=3289

s.connect((host,port))

while True:
	data=input(">>>")
	s.send(data)
	val=s.recv(1024)
	print('The received data is',val)
s.close()
