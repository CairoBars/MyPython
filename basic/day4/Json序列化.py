#Author:Cairo Li

import json
import pickle

def sayhi(name):
    print("Hello,",name)

info={
    'name':'alex',
    'age':22,
    #'func':sayhi
    # 用pickle可以序列化所有东西，不过函数在反序列化时
    #需要自己再定义一个同名的函数
}


#同一个文件只能dump一次，否则反序列化时会出错
f=open("test.test","w")
#f.write(pickle.dumps(info))
f.write(json.dumps(info))
f.close()