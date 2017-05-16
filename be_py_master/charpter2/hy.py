class MetaInporter(object):
	'''Hy模块导入器'''
	def find_on_path(self,fullname):
		fls=["%s__init__.hy","%s.hy"]
		dirpath="/".join(fullname.split("."))

		for pth in sys.path:
			pth=os.path.abspath(pth)
			for fp in fls:
				composed_path=fp % ("%s/%s" %(pth,dirpath))
				if os.path.exists(composed_path):
					return composed_path

	def find_module(self,fullname,path=None):
		path=self.find_on_path(fullname)
		if path:
			return MetaInporter(path)


sys.meta_path.append(MetaInporter())

