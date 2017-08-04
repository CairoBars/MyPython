#Author:Cairo Li
"""
__iter__
如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()
方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的
__next__()方法拿到循环的下一个值，直到StopIteration错误时退出循环
"""
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1#初始化计数器

    def __iter__(self):
        return self #实例本身就是迭代对象，所有返回自己

    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>10:
            raise StopIteration()
        return self.a

for n in Fib():
   print(n)

"""
Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是
不行，比如取某下标的元素
"""

class Fib2(object):
    def __getitem__(self,n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
        return a

f2=Fib2()
print(f2[0])

#添加切片功能
class Fib3(object):
    def __getitem__(self, item):
        if isinstance(item,int):  #item是索引
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(item,slice):
            start=item.start
            stop=item.step
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b=b,a+b
            return L

"""
__getattr__
当调用不存在的属性时，比如score，Python解释器
会自动调用__getattr__(self,'score')来获取属性
"""

class Student(object):
    def __getattr__(self, attr):
        if attr=='age':
            return lambda:25
        raise AttributeError('\'Student\' object has no attribute \'%s\''%attr )

s=Student()
print(s.age)
print("---")
#print(s.nn)

class Chain(object):
    def __init__(self,path=''):
        self._path=path
    def __getattr__(self, path):
        return Chain('%s/%s'%(self._path,path))
    def __str__(self):
        return self._path

    __repr__=__str__

a=Chain().c.myGame.LOL.list
print(type(a))
print(a)

