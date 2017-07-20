#Author:Cairo Li
class Dog(object):
    name='GGG'
    def __init__(self):
        self.name='VVV'


    @staticmethod #本质上不属于这个类里，
    # 也不能访问这个类或对象的属性，除非传参数进去
    def talk():
        print(Dog.name)

    @classmethod
    def talk2(self):
        print(self.name)    #只能访问类属性





    #将方法变成静态属性，并且不可以对eat赋值（其实是传参)
    @property
    def eat(self):
        print("eat")

    @eat.setter
    def eat(self,gg):
        #可进行赋值操作
        self.__gg = gg
        print('eat',self.__gg)

    @eat.deleter
    def eat(self):
        del self.__gg
        print("删除完毕")


d=Dog()
d.talk()
Dog.talk()
Dog.talk2()
d.talk()
d.eat=4
del d.eat