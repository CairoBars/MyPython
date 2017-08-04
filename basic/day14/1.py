import os



class MyPath():
    @classmethod
    def __fspath__(cls,path):
        return path

print(type(MyPath)) #<class 'type'>
p=MyPath()
print(type(p))  #<class '__main__.MyPath'>
p_type=type(p)
path="fdsf"
path_repr=p_type.__fspath__(path)   #输出fdsf
print(path_repr)




b=os.PathLike


c=str('C:\dsfdsfs')

print(dir(c))
#print(os.path.join())

#Join two(or more)paths
def join(path,*paths):
    path=os.fspath(path,bytes)

class A():
    def __UU__(self):
        print("UU")
    def _B(self):
        pass


a=A()
a_type=type(a)



a_type.__UU__(a)
print(a_type.__name__)
print(hasattr(a_type,'__UU__')) #True
print(hasattr(A,'__UU__'))      #True
print(hasattr(a,'__UU__'))      #True
try:
    a_type.__UU__()
except AttributeError:
    if hasattr(a_type,'__UU__'):
        print("SSS")
        raise





def _fspath(path):
    if isinstance(path,(str,bytes)):
        return  path
    path_type=type(path)
    try:
        path_repr=path_type.__fspath__(path)
    except AttributeError:
        if hasattr(path,'__fspath__'):
            raise
        else:
            raise TypeError("expected str,bytes or os.PathLike object,"
                            "not"+path_type.__name__)
    if isinstance(path_repr,(str,bytes)):
        return path_repr
    else:
        raise TypeError("expected {}.__fspath__() to return str or bytes,"
                        "not {}".format(path_type.__name__,type(path_repr).__name__))