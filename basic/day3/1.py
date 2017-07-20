#-*- coding:utf-8 -*-
from multiprocessing import Process
import os

#字进程要执行的代码、
def run_proc(name):
        print("GFFF")
        print('Run child process %s(%s)...'%(name,os.getpid()))


	
if __name__=='__main__':
	print('Parent process %s' %os.getpid())
	p=Process(target=run_proc,args=('test',))
	print('Child process will start')
	p.start()
	print("moliao shi sb")
	p.join()
	print('Child process end')
