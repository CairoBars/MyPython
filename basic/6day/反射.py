#Author:Cairo Li
#通过字符串映射或修改程序运行时的状态、属性、方法，有一下4个方法
#getattr(object,name,default=None)
#hasattr(object,name)
#setattr(x,y,v)
#delattr(x,y)

def newfun():
    print("I am new func")

class Dog(object):
    def __init__(self,name):
        self.name=name

    def eat(self):
        print("%s is eating...",self.name)


choice="rr"
d=Dog("GG")

if hasattr(d,choice):
    getattr(d,choice)()
else:
    setattr(d,choice,newfun) #相当于 d.choice=newfun  所以是d.choice()调用函数
    d.rr()
    delattr(d,choice)
    #d.rr()
    print(d.name)
    setattr(d,"yy",33)
    print(d.yy)
    setattr(d,'name',2333)
    print(d.name)