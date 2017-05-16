'''Using a Class as a Decorator'''
#We will rewrite the following decorator as a class:
def decorator1(f):
    def helper():
        print("Decorating", f.__name__)
        f()
    return helper

@decorator1
def foo():
    print("inside foo()")

foo()
#The following decorator implemented as a class does the same "job":
class decorator2(object):
    
    def __init__(self, f):
        self.f = f
        
    def __call__(self):
        print("Decorating", self.f.__name__)
        self.f()

@decorator2
def foo():
    print("inside foo()")

foo()
#   Both versions return the same output:
#   Decorating foo
#   inside foo()