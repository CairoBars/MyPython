def fibonacci(n):
	"""Fibonacci numbers generator ,first n"""
	a,b,counter=0,1,0
	while True:
		if (counter>n):return
		yield a
		a,b=b,a+b
		counter+=1

'''
f=fibonacci(5)

for x in f:
	print x,
'''

def fibonacci2():
	"""Fibonacci numbers generator"""
	a,b=0,1
	while True:
		yield a
		a,b=b,a+b

f=fibonacci2()

counter=0
for x in f:
	print x,
	counter+=1
	if(counter>10):break
print