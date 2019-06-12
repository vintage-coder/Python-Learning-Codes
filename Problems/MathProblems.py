#Quadratic Equation 

import cmath
print("Quadratic Equation Solution")
a=int(input("Enter the coordinate for x2"))
b=int(input("Enter the coordinate for x"))
c=int(input("Enter the coordinate for constant"))

temp=a*a-4*a*c

x1=(-b-cmath.sqrt(temp))/(2*a)
x2=(-b+cmath.sqrt(temp))/(2*a)

print("The solutions of the given quadratic equation is{} and {}".format(x1,x2))

print("Fibonascii Series")

num=int(input("Enter the number:"))
a=0
b=1
print(a)
print(b)
for i in range(num):
	a,b=b,a+b
	print(b)

print("Prime Numbers Solutions")

num=int(input("Enter the number to find the Prime number"))


for i in range(2,num):
	if num%i==0:
		print("The given number {} is not a prime number".format(num))
		break

if i==num-1:
	print("The given number {} is a prime number".format(num))

