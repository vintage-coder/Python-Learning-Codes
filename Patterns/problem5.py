val=int(input('Enter the number:'))

for i in range(2*val-1,1,-1):
	for j in range(1,val):
		for k in range(1,j):
			print(k,end=' ')
		print('')
	for l in range(val-1,1,-1):
		for m in range(1,l):
			print(m,end=' ')
		print('')
	