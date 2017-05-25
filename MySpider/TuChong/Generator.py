#_*_ coding:utf-8 _*_

def odd(n):
	"""Generate certain numbers of odd"""
	count=0
	start=1
	while True:
		yield start
		start+=2
		count+=1
		if count==n:break



#当然也可以手动写一个迭代器：
class Iter:
	def __init__(self):
		self.start=-1
	def __iter__(self):
		return self
	def __next__(self):
		self.start+=2
		return self.start


#saveOdd=odd(3)
#print list(saveOdd)

I=Iter()
for i in range(5):
	print (next(I))