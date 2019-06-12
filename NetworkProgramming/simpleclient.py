import socket

s=socket.socket()

port =12345
s.connect(('127.0.0.1',port))


print('The received data is :',s.recv(1024))

s.close()
