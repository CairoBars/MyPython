#Author:Cairo Li
'''
A metaclass is the class of a class.
Like a class defines how an instance of the class behaves,
a metaclass defines how a class behaves.
A class is an instance of a metaclass.
url:https://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python
'''



#__new__先于__init__执行
class Foo(MyType):
    __metaclass__=MyType

    def __init__(self,name):
        self.name=name
        print("Foo --init--")
    def __new__(cls, *args, **kwargs):#cls相当于Foo这个类
        print("--new--")
        return MyType.__new__(cls)  #这句注释掉之后将不会执行__init__
        #所以new是用来创建实例的，而init则是初始化实例



f=Foo("AA")



