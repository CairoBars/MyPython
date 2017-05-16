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

