#Author:Cairo Li
def myGG(**kwargs):
    return kwargs

gmethods=myGG(methods=['get','post'])
vv=gmethods.pop('methods',None)
print(vv)


result=set(item.upper() for item in vv)
print(result)


myset=set(['a','b'])
myset|={'c'}
print(myset)