#Author:Cairo Li
import gevent
def func1():
    print('\033[31;1m GGGGG...\033[0m')
    gevent.sleep(2)
    print('\033[31;1mEEEEEEEE....\033[0m')

def func2():
    print('\033[32;1mRRRRRRRRRR...\033[0m')
    gevent.sleep(1)
    print('\033[32;1mUUUUUUUUUUUUU...\033[0m')

gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2)
    ]
)