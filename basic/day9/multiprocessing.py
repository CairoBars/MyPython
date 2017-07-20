#Author:Cairo Li
#python多线程 不适合CPU密集操作型的任务，适合IO操作密集型的任务
#python进程和线程都用的是操作系统原生的进程和线程，原生的是由操作系统自己维护的

#python的多进程可以使用CPU的多核

#多进程间的通行: from multiprocessing import Queue,从multiprocessing中导入Queue跟普通的Queue用法差不多

#Queue 、Pipe只实现进程间数据的传递
#Manager实现了进程间数据的共享，即多个进程可以修改同一份数据




from multiprocessing import  Process ,Queue
import  threading
#import queue

'''
用Queue（进程的Queue）对象作为参数传递给另一个进程时，
其实是python通过pickle实现参数序列化，然后再复制一份到另一个进程中，
因为两个进程是不能共享内存的。
而普通的queue作为参数传递给另一个进程时，则会报错。
'''

def f(qq):
    print("in chlid:",qq.qsize())
    qq.put([42,None,'hello'])

# p = threading.Thread(target=f,)
p = Process(target=f, args=(q,))
p.start()
p.join()
print("444", q.get_nowait())
print("444", q.get_nowait())
# prints "[42, None, 'hello']"
#p=threading.Thread(target=f,args(q,))