'''
The way we have defined decorators so far hasn't taken into account that the attributes
__name__ (name of the function),
__doc__ (the docstring) and
__module__ (The module in which the function is defined)
of the original functions will be lost after the decoration. 

The following decorator will be saved in a file greeting_decorator.py:
'''

def greeting(func):
	def function_wrapper(x):
		"""function_wrapper of greeting"""
		print("Hi, "+func.__name__+" returns:")
		return func(x)
	return function_wrapper

#We call it in the following program:
from greeting_decorator import greeting
@greeting
def f(x):
	"""just some silly function"""
	return x+4
f(10)
print("function name:"+f.__name__)
print("docstring:"+f.__doc__)
print("module name:"+f.__module__)

#	We get the follwoing unwanted results:
#	Hi, f returns:
#	function name: function_wrapper
#	docstring:  function_wrapper of greeting 
#	module name: greeting_decorator

'''We can save the original attributes of the function f, if we assign them inside of the 
decorator. We change our previous decorator accordingly and save it as greeting_decorator_manually.py:'''
def greeting(func):
	def wrapper(x):
		"""function_wrapper of greeting"""
		print("Hi, "+func.__name__+" returns:")
		return func(x)
	wrapper.__name__=func.__name__
	wrapper.__doc__=func.__doc__
	wrapper.__module__=func.__module__
	return wrapper
#	Now we get the proper results:
#	Hi, f returns:
#	function name: f
#	docstring:  just some silly function 
#	module name: __main__