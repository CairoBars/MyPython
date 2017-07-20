#Author:Cairo Li
import threading
import time

def run(n):
    print("task",n)
    time.sleep(2)
    print("task done",n,threading.current_thread())

start_time=time.time()
t_objs=[]
for i in range(50):
    t=threading.Thread(target=run,args=("t-%s"%i,))
   # t.setDaemon(True)#把当前线程设置成守护进程
    #设置成守护线程，主线程退出后，不管子线程有没有执行完，子线程都会结束
    t.start()
    t_objs.append(t)


print("-----all threads has finished...",threading.current_thread(),threading.active_count())
print("cost:",time.time()-start_time)