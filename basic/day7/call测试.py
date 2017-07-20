#Author:Cairo Li
'''
关于__call__方法的调用，因为Foo是Singleton的一个实例。所以Foo()这样的方式就调用了Singleton的__call__方法。
不明白就回头看看上一节中的__call__方法介绍。
'''

class Singleton(object):
    def __call__(self, *args, **kwargs):
        print("Singleton Call")

class Foo(Singleton):
    def __call__(self, *args, **kwargs):
        print("Foo Call")


#总结：如果子类定义了call方法则只调用子类的call方法，如果没定义就调用父类的

f=Foo()
f()