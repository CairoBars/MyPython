

'''
Python��������������һ��һ���Ƕ�׵ģ�����˵��������ǲ�����������ⷵ���������������ϲ���

'''
age=22
names['alex','jack'] #������Է��ʣ�Ϊʲô�أ� ����Ƶ��
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
	print(*args)	#���Ԫ��
	print(**kwargs)


#�ݹ�
#1.��ȷ�Ľ�������
#2.�����ģÿ�ݹ�һ�ζ�Ӧ�ñ���һ�ε������ģ����
#3.Ч�ʵ�

#�߽׺���������һ��������������������һ������

#����ʽ��̣�

#��utf-8�ı��Զ����Ʒ�ʽд���ļ�(һ���ڿ�ƽ̨ʱ��Linux�ļ���Windows�ϴ�������Ƶ�����ļ�)
open('text.txt','wb',encoding='utf-8')	