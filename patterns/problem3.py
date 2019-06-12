val=int(input('Enter the number:'))

count=0
for i in range(val,0,-1):
	for j in range(1,i):
		print(j,end='')
	count+=1
	print('')
	for k in range(count):
		print('',end=' ')

print('')