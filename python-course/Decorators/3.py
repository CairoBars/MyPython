'''
So far we used functions as decorators. Before we can define a decorator as a class, we have to introduce the __call__ method of classes. 
We mentioned alreaedy that a decorator is simply a callable object that takes a function as an input parameter. 
A function is a callable object, but what lots of Python programmers don't know. We can define classes as callable objects as well.
 The __call__ method is called, if the instance is called "like a function", i.e. using brackets.
'''

class A:
	def __init__(self):
		print("An instance of A was initialized")
	def __call__(self,*args,**kwargs):
		print("Arguments are:",args,kwargs)

x=A()
print("now calling the instance:")
x(3,4,x=11,y=10)
print("Let's call it again:")
x(3,4,x=10,y=10)

#	We get the following output:
#	An instance of A was initialized
#	now calling the instance:
#	Arguments are: (3, 4) {'x': 11, 'y': 10}
#	Let's call it again:
#	Arguments are: (3, 4) {'x': 11, 'y': 10}

#We can write a class for the fibonacci(斐波那契) function by using __call__:
class Fibonacci:
	def __init__(self):
		self.cache=[]
	def __call__(self,n):
		if n not in self.cache:
			if n==0:
				self.cache[0]=0
			elif n==1:
				self.cache[1]=1
			else:
				self.cache[n]=self.__call__(n-1)+self.__call__(n-2)
		return self.cache[n]

fib=Fibonacci()

for i in range(15):
	print(fib(i),end="")

#	The output:
#	0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 