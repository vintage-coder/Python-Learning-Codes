import socket

s=socket.socket()

port =12345

print("socket sucessfully created............")

s.bind(('',port))

print('socket was bounded in %s'%port)
s.listen(5)
print('socket is listening.............')

while True:
	c,addr=s.accept()
	print('got conection from ',addr)
	print('got conection from ',c)
	c.send(b'Thank you for connecting.....')
	c.send(b'hi gowthaman this is a simple server....')
c.close()

