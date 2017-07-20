#Author:Cairo Li

class MyException(Exception):
    def __init__(self,msg):
        self.message=msg
    '''
    def __str__(self):
        return self.message
    '''

try:
    raise  MyException("GGSIMIDA") #自定义异常需要自己调用
except MyException as e:
    print(e)