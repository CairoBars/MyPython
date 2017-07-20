#Author:Cairo Li

class A(object):
    country="China"

    def __init__(self,name,count):
        self.name=name
        self.count=count
    '''
    特斯拉
    '''
    def __call__(self, *args, **kwargs):
        pass


#__doc__显示特使拉，类的描述
#__module__ 表示当前操作的对象在哪个模块
#__class__ 表示当前操作的对象的类是什么
#__call_
#__dict__   显示类或对象里边的所有成员
a=A('a',22)
a() #调用call方法
A('a',33)()#调用call方法

print(a.__dict__)#打印对象属性 {'name': 'a', 'count': 22}
print(A.__dict__)#打印类成员和属性

#__str__()如果一个类中定义了__str__方法，那么在打印对象时
#默认输出该方法的返回值


#用于索引操作，如字典：一下分别表示获取、设置、删除数据
#可以实现自定义字典？大概吧
class Foo(object):
    def __getitem(self,key):
        print('__getItem__',key)
    def __setitem__(self, key, value):
        print('_setItem',key,value)
    def __delitem__(self, key):
        print('__delitem__',key)

obj=Foo()
result=obj['k1']    #自动触发执行__getitem__
obj['k2']='alex'    #自动触发执行__setitem__
del obj['k1']
