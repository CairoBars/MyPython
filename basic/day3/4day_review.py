

'''
Python变量的作用域是一层一层的嵌套的，就是说如果里面那层有这个变量这返回这个，否则就往上层找

'''
age=22
names['alex','jack'] #这个可以访问，为什么呢？ 看视频吧
def show():
	age=25
	print(age)	#25

print(age)	#22

def show2():
	print(age)	#22

def show3():
	global age
	age=29
	names.append(33)
	print(names)
	print(age)


def testargs(gg,vv,*args,**kwargs)
	print(gg,vv)
	print(*args)	#输出元组
	print(**kwargs)


#递归
#1.明确的结束条件
#2.问题规模每递归一次都应该比上一次的问题规模减少
#3.效率低

#高阶函数：把另一个函数当做参数传给另一个函数

#函数式编程：

#将utf-8文本以二进制方式写入文件(一般在跨平台时，Linux文件到Windows上处理，或视频流等文件)
open('text.txt','wb',encoding='utf-8')	