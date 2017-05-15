"""文件和异常处理"""
with open('digit.txt') as file_object:
	contents=file_object.read()
#read读取到文件末尾会多出一个空行，所有用rstrip删除多余的空行
	print(contents.rstrip())

#在Linux和MAC中
with open('text_files/filename.txt') as file_object:
	print()

#在Windows中
with open('text_files\filename.txt') as file_object:
	print()


#逐行读取
with open(filename) in file_object:
	for line in file_object:
		print(line.rstrip())

#创建一个包含文件各行内容的列表
with open(filename) as file_object:
	lines=file_object.readlines()
for line in lines
	print(line.rstrip())