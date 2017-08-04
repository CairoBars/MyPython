#Author:Cairo Li
"""
如果我们要限制实例的属性怎么办？比如只运行Student实例添加name，age属性
"""
class Student(object):
    __slots__ = ('name','age')
    pass


Student.oo="GG"
print(Student.oo)

stu=Student()
stu.gg="GG"