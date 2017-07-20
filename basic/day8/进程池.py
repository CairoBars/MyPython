#Author:Cairo Li
#进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，如果进程池序列中没有可
#提供使用的进程，那么程序就会等待，直到进程池中有可用进程为止
from multiprocessing import Process,Pool
import time
import os
def Foo(i):
    time.sleep(2)
    return i+100

def Bar(arg):
    print('-->exec done',arg,os.getpid())

pool=Pool(5)

for i in range(10):
    #主进程执行回调函数，可以通过主进程写个链接数据库实例的方法，然后子进程调用
    pool.apply_async(func=Foo,args=(i,),callback=Bar)


print('end')
pool.close()
pool.join()#线程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭