#Author:Cairo Li
#文件只能存储二进制或字符串
#Json.dump()对一个文件只dump一次，dump多次在读的时候会报错
adit={'a':'A','b':'B'}
sdit=str(adit)
print(sdit)     #"{'a': 'A', 'b': 'B'}"
adit2=eval(sdit)
print(adit2)    #{'a':'A','b':'B'}
