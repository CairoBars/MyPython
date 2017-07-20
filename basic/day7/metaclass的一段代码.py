#Author:Cairo Li
#摘自：http://www.cnblogs.com/tkqasn/p/6524879.html

class Singleton(type):
    def __init__(self, *args, **kwargs):
        print "__init__"
        self.__instance = None
        super(Singleton,self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        print "__call__"
        if self.__instance is None:
            self.__instance = super(Singleton,self).__call__(*args, **kwargs)
        return self.__instance


class Foo(object):
    __metaclass__ = Singleton #在代码执行到这里的时候，元类中的__new__方法和__init__方法其实已经被执行了，而不是在Foo实例化的时候执行。且仅会执行一次。


foo1 = Foo()
foo2 = Foo()
print Foo.__dict__  #_Singleton__instance': <__main__.Foo object at 0x100c52f10> 存在一个私有属性来保存属性，而不会污染Foo类（其实还是会污染，只是无法直接通过__instance属性访问）

print foo1 is foo2  # True

# 输出
# __init__
# __call__
# __call__
# {'__module__': '__main__', '__metaclass__': <class '__main__.Singleton'>, '_Singleton__instance': <__main__.Foo object at 0x100c52f10>, '__dict__': <attribute '__dict__' of 'Foo' objects>, '__weakref__': <attribute '__weakref__' of 'Foo' objects>, '__doc__': None}
# True