#Author:Cairo Li
import  threading

class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__(self)
        self.n=n
    def run(self):
        print("running task",self.n)

t1=MyThread("t1")
t2=MyThread("t2")