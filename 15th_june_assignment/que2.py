# QUESTION 2:
class A:
	def f(self):
		return self.g()    # calling its own method g()
	def g(self):
		return 'A'


class B(A):
	def g(self):
		return 'B'

object_A = A()     # creating object of class A
object_B = B()      # creating object of class B
print(object_A.f(), object_B.f())
print(object_A.g(), object_B.g())


 # output : A B
 #          A B