class Dict(dict):
	def __init__(self,**kw):
		super(Dict,self).__init__(**kw)

	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"Dict's object has no attribute '%s'"%key)
	def __setattr__(self,key,value):
		self[key]=value


#self.assertEquals(abs(-1),1) 断言函数返回的结果与1相等

import unittest
class TestDict(unittest.TestCase):
	def test_init(self):
		d=Dict(a=1,b='test')
		self.assertEquals(d.a,1)
		self.assertEquals(d.b,'test')
		self.assertTrue(isinstance(d,dict))

	def test_key(self):
		d=Dict()
		d['key']='value'
		self.assertEquals(d.key,'value')

#断言抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出keyError
	def test_attr(self):
		d=Dict()
		with self.assertRaises(KeyError):
			value=d['empty']

#通过d.empty访问不存在的key时，我们期待抛出AttributeError
	def test_attrerror(self):
		d=Dict()
		with self.assertRaises(AttributeError):
			value=d.empty


if __name__=='__main__':
	unittest.main()