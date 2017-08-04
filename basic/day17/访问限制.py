#Author:Cairo Li

class Student(object):
    __name="GG"

    #_[name]按照约定俗成的规定，当你看到这样的变量时，意思就是：
    #'虽然我可以被访问，但是，请把我视为私有变量，不要随意访问'
    _name="RR"


#print(Student.__name)
print(Student._Student__name)
print(Student._name)

#虽然表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量
#和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器
# 自动地改成了_Student__name
Student.__name="EE"
print(Student.__name)