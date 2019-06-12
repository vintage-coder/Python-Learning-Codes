import socket

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
except socket.error as err:
	print('socket not created due to error %s'%err)

host="127.0.0.1"
port=3289
s.bind((host,port))
# s.listen(5)
# c,addr=s.accept()

while True:
	data=s.recv(1024)
	print("The received data is ",data)
	val=input(">>>")
	s.send(val)

s.close()
