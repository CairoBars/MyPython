#Author:Cairo Li
import os
import sys
print(__file__) #打印的是相对路径，相对于Python执行这个文件时Python所在的目录

#os.path.dirname:返回上一级目录名
BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


#可以使用Json序列化（跨平台使用），也可以使用pickle序列化（Python之间使用）