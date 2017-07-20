#Author:Cairo Li




try:
    a='gg'

#2.7的写法：try IOError,e: 在3.0中必须用as
except (IOError,IndexError) as e:
    print(e)
except Exception as e: #这个一般写在最后面啦
    print("啥错呢",e)
else:
    print("没有错误发生")
finally:
    print("不管有没有错都要执行的啦")