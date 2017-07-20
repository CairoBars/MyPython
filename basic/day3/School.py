#! -*- coding:utf-8 -*-
#__author__:"Cairo Li"

class School(object):
	members=0	#��ʼ��ѧУ����Ϊ0
	def __init__(self,name,addr):
		self.name=name
		self.addr=addr
		self.students=[]
		self.teachers=[]
	
	
	def enroll(self,stu_obj):
		'''ע��'''
		SchoolMember.menbers+=1
		print("ΪѧԱ%s ����ע������"%stu_obj.name)
		self.students.append(stu_obj)


class SchoolMember(object):

	def __init__(self,name,age,sex):
		self.name=name
		self.age=age
		self.sex=sex

	def tell(self):
		pass



class Teacher(SchoolMember):
	def __init__(self,name,age,sex,salary,course):
		super(Teacher,self).__init__(name,age,sex)
		self.salary=salary
		self.course=course
	
	def tell(self):
		print('''
		----info of Teacher:%s----
		Name:%s
		Age:%s
		Sex:%s
		Salary:%s
		Course:%s
		'''%(self.name,self,name,self.age,self.sex,self.salary,self.course)
	
	def teach(self):
		print(%s is teaching course [%s]"%(self.name,self.course))


class Student(SchoolMember):
	def __init__(self,name,age,sex,stu_id,grade):
		super(Student,self).__init__(name,age,sex)
		self.stu_id=stu_id
		self.grade=grade
	
	def tell(self):
		pass
	
	def pay_tuition(self,amount):
		print("%s has paid tuition for $ ")
