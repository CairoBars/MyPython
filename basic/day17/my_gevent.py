#Author:Cairo Li
"""
Python通过yield提供了对协程的支持，但是不完全。第三方gevent为Python提供了
比较完善的协程支持
"""
#由于切换是在IO操作时自动完成，所有gevent需要修改Python自带的一些标准库，
# 这一过程在启动时通过monkey patch完成：

from gevent import monkey;monkey.patch_all()
import gevent

def Fun(n):
    for i in range(n):
        print(gevent.getcurrent(),i)

g1=gevent.spawn(Fun,5)
g2=gevent.spawn(Fun,5)
g3=gevent.spawn(Fun,5)
g1.join()
g2.join()
g3.join()

#上面程序顺序执行
def Fun2(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        gevent.sleep()#主动切换协程

import urllib2

def Fun3(url):
    resp=urllib2.urlopen(url)
    data=resp.read()

gevent.joinall([
    gevent.spawn(Fun3,'http://www.python.org'),
    gevent.spawn(Fun3,'https://www.yahoo.com'),
    gevent.spawn(Fun3,'https://github.com')

])


