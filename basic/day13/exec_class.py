#Author:Cairo Li
class A(object):
    __a='ddd'
    _v='wacha'
    def __init__(self):
        print(A._v)
        self.__b='rrr'
    def getAttr(self):
        print(self.__b)
        return A.__a
    @classmethod
    def gg(cls,self):
        #print(cls.__name__)
        #print("GGSIMIDA")
        #print(cls.__a)
        print(self.__b)

    @staticmethod
    def hh():
        print("FFF")


a=A()
A.v
A.gg(a)