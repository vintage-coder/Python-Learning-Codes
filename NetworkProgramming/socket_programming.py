import socket
import sys

#This is the socket object for making a communication with server
# AF_INET  is the address family default it says ipv4 and SOCK_STREAM is for TCP oriented connection
try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print("Socket successfully was created.......")
except socket.error as err:
	print('socket creation failed with error {}'.format(err))

port = 80

try:
	ip=socket.gethostbyname("www.google.com")
except socket.gaierror:
	print("There was an error when resolving the host")

s.connect((ip,port))
print("The socket successfully connected to google by ip {} and port is {}".format(ip,port))
print(s)
print('The ip of goole is :',ip)



