'''
Summarizing we can say that a decorator in Python is a callable Python object that is used to modify a function, 
method or class definition. The original object, the one which is going to be modified, is passed to a decorator as an argument. 
The decorator returns a modified object, e.g. a modified function, which is bound to the name used in the definition.
'''
from math import sin,cos

def our_decorator(func):
	def function_wrapper(x):
		print("Before calling "+func.__name__)
		func(x)
		print("After calling "+func.__name__)
	return function_wrapper

def foo(x):
	print("Hi , foo has been called with "+str(x))

print("We call foo before decoration:")
foo("Hi")

print("We now decorate foo with f:")
foo=our_decorator(foo)

print("We call foo after decoration:")
foo(42)

#uper function result:
'''
We call foo before decoration:
Hi, foo has been called with Hi
We now decorate foo with f:
We call foo after decoration:
Before calling foo
Hi, foo has been called with 42
After calling foo
'''

'''
We will rewrite now our initial example.Instead of writing the statement:
foo=our_decorator(foo)
we can write:
@our_decorator

'''


'''
It is also possible to decorate third party functions, e.g. functions 
we import from a module. We can't use the Python syntax with the "at" sign in this case:'''
def my_decorator(func):
	def function_wrapper(x):
		print("Before calling "+func.__name__)
		res=func(x)
		print(res)
		print("After calling "+func.__name__)
	return function_wrapper
sin =my_decorator(sin)
cos=my_decorator(cos)
