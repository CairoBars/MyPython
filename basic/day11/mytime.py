#Author:Cairo Li
import gevent,time

def task(pid):
    gevent.sleep(0.5)
    print("Task %s done"%pid)

def synchronous():
    for i  in range(1,10):
        task(i)

def asynchronous():
    threads=[gevent.spawn(task,i) for i in range(10)]
    gevent.joinall(threads)

start_time=time.time()
synchronous()
print("syn time is %s",time.time()-start_time)

start_time=time.time()
asynchronous()
print("asyn time is %s",time.time()-start_time)