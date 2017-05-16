class MetaLoader(object):
	'''Hy模块加载器'''
	def __init__(self,path):
		self.path=path

	def is_package(self,fullname):
		dirpath="/".join(fullname.split("."))
		for pth in sys.path:
			pth=os.path.abspath(pth)
			composed_path="%s/%s/__init__.hy"%(pth,dirpath)
			if os.path.exists(composed_path):
				return True
		
		return False

	def load_module(self,fullname):
		if fullname in sys.modules:
			return sys.modules(fullname)
		if not self.path:
			return

		sys.modules[fullname]=None
		#import_file_to_module读取一个Hy源文件，将其编译成Python代码，并返回一个Python模块对象
		mod=import_file_to_module(fullname,self.path)

		ispkg=self.is_package(fullname)

		mod.__file__=self.path
		mod.__loader__=self
		mod.__name__=fullname

		if ispkg:
			mod.__path__=[]
			mod.__package__=fullname
		else:
			mod.__package__=fullname.rpartition('.')[0]

		sys.modules[fullname]=mod
		return mod