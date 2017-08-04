#Author:Cairo Li
"""
greenlet 是一个C实现的协程模块，相比于python自带的yield，
它可以使你在任意函数之间随意切换，而不需要把这个函数先声明为generator
"""
from gevent import monkey; monkey.patch_socket()
from greenlet import greenlet

def test1():
    print(12)
    gr2.switch()
    print(45)
    gr2.switch()

def test2():
    print(56)
    gr1.switch()
    print(55)


gr1=greenlet(test1)
gr2=greenlet(test2)
gr1.switch()