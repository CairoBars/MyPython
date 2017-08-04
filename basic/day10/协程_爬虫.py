#Author:Cairo Li

from urllib import request
import  gevent

'''
默认gevent不识别url加载网页的操作为IO操作，所有使用money将所有可能与
IO操作的对象设置标记，然后才能进行异步
'''