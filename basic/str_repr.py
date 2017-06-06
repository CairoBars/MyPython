import os
class Dog:
	def __repr__(self):
		return "I am repr"
	def __str__(self):
		return "I am str"

d=Dog()
print(d)
print(str(d))
print("%r"%d)

basedir=os.path.abspath(os.path.dirname(__file__))
gg=os.path.join(basedir,'ggg')
print(basedir)
print(gg)