#Diomand Problem
class E:
	def call_me(self):
		print("This is the E function")
class F(E):
	def call_me(self):
		E.call_me(self)
		print('This is F function')

class G(E):
	def call_me(self):
		E.call_me(self)
		print('This is the G Function')

class H(F,G):
	def call_me(self):
		F.call_me(self)
		G.call_me(self)
		print("This is the H function")


if __name__=="__main__":
	obj=H()
	obj.call_me()





print("==============================The solution to this Problem=======================")

# Using the super of function



#Solution
class A:
	def call_me(self):
		print("Bass function")
		

class B(A):
	def call_me(self):
		super().call_me()
		print("This is B function")
class C(A):
	def call_me(self):
		super().call_me()
		print("This is C function")
class D(B,C):
	def call_me(self):
		super().call_me()
		
		print("This is D function")


if __name__=="__main__":
	obj=D()
	obj.call_me()


