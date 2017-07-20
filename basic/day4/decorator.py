#Author:Cairo Li

'''
def mydec(func):
    def wrapper(*args,**kwargs):
        print("AAAA")
        func()
    return wrapper
'''

def gg(flag):
    def mydec(func):
        def wrapper(*args,**kwargs):
            if flag:
                print("AAAA")
            else:
                print("BBBBB")
            func()
        return wrapper
    return mydec

@gg(flag=False)
def show():
    print("强哥是傻逼")

show()