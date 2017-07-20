#Author:Cairo Li

import threading,time

start_time=time.time()

def run(n):
    time.sleep(1)
    print(n)


t_objs=[]

for i in range(50):
    t=threading.Thread(target=run,args=(i,))
    t.start()
    t_objs.append(t)


for t in t_objs:
    t.join()

'''
while True:
    if threading.active_count()==1:break
'''
end_time=time.time()

print("一共的时间是：",end_time-start_time)

#上面两种方法的执行结果都接近1S

