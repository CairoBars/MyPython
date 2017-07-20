
import sys
print(sys.getdefaultencoding()) #输出为utf-8

msg="我是程序"
#msg_gb2312=msg.decode('utf-8').encode('gb2312')
msg_gb2312=msg.encode('gb2312')#默认就是Unicode不用decode
gb2312_to_unicode=msg_gb2312.decode('gb2312')
gb2312_to_utf8=msg_gb2312.decode("gb2312").encode("utf-8")

print(msg_gb2312)
print(str(msg_gb2312).count('\\')) #unnicode 中文3个字节
print(gb2312_to_unicode)
print(gb2312_to_utf8)
print(str(gb2312_to_utf8).count('\\')) #utf-8 中文两个字节
