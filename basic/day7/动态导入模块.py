#Author:Cairo Li

import importlib

lib=importlib.import_module('lib.app') #官方建议使用这个
lib=__import__('lib.app')
