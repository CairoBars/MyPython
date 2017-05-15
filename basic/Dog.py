class Dog():
	"""Pythonz中根据约定，首字母大写的名称是类"""
	"""以self为前缀的变量可供类中所有方法使用"""
	def __init__(self,name,age0):
		self.name=name
		self.age=age

	def sit(self):
		print()

	def roll_over(self):
		print(self.name)