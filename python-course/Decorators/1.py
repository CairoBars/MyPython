def argument_test_natural_number(f):
	def helper(x):
		if type(x)==int and x>0:
			return f(x)
		else:
			raise Exception("Agrument is not an integer")
	return helper

@argument_test_natural_number
def factorial(n):
	if n==1:
		return 1
	else:
		return n*factorial(n-1)

for i in range(1,10):
	print(i,factorial(i))
'''The following example uses a decorator to count the number of times a function has been called.

To be precise,we can use this decorator soley for functions with exactly one parameter'''
#实现程序调用的计数
def call_counter(func):
	def helper(x):
		helper.calls+=1
		return func(x)
	helper.calls=0
	return helper
@call_counter
def succ(x):
	return x+1

print(succ.calls)
for i in range(10):
	print(succ(i))
print(succ.calls)



#write again 1 time
def call_counter(func):
	def helper(x):
		helper.calls+=1
		return func(x
	helper.calls=0
	return helper

@call_counter
def succ(x):
	reutrn x+1

print(succ.calls)
for i in range(10)):
	print(succ(i))
print(succ.calls)


#write again 2 times:
def call_counter(func):
	def count(x):
		count.calls+=1
		return func()
	count.calls=0
	return count

@call_counter
def sum(x):
	return x+1


#previous decorator only for function ,which take exactly one parameter.
#We will use the *args and **kwargs notation to write decorators which can
#code with functions with an arbitrary number of positional and keyword parameters

def call_counter(func):
	def helper(*args,**kwargs):
		helper.calls+=1
		return func(*args,**kwargs)
	helper.calls=0
	reutrn helper

@call_counter
def mull(x,y=1):
	return x+y

mull(2,3)
mull(1,1)
print(mull.calls)


def greet_evening(func):
	def greet_wrapper(*args,**kwargs):
		print("Good enening!")
		return func(*args,**kwargs)
	return greet_wrapper

def greet_morning(func):
	def greet_wrapper(*args,**kwargs):
		print("Good Morning!")
		return func(*args,**kwargs)
	return greet_morning

@greet_morning
def test(x):
	print(x)


#带参数的decorator,就是外面包了一层函数，来接收参数：
def greeting(expr):
	def greeting_decorator(func):
		def wrapper(*args,**keyword):
			print("Good"+expr)
			func(x)
		return greeting_decorator
	return greeting

@greeting("Morning")
def test2(x):
	print(x)

