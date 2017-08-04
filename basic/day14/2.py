#Author:Cairo Li

import os



c=b'dddd'
print(type(c))  #<class 'bytes'>
f="fdfd"
print(b'ddd')
print('ddd')
sep='\\'
print(sep)






def splitdrive(p):
    p=os.fspath(p)
    if (len)>=2:
        if isinstance(p,bytes):
            sep=b'\\'
            altsep=b'/'
            colon=b':'
        else:
            sep='\\'
            altsep='/'
            colon=':'
        normp=p.replace(altsep,sep)
        if(normp[0:2]==sep*2) and (normp[2:3]!=sep):
            index=normp.find(sep,2) #找第3个元素
            if index==-1:
                return p[:0],p
            index2=normp.find(sep,index+1)
            # a UNC path can't have two slashed in a row
            #(after the initial two)
            if index2==index+1:
                return p[:0],p
            if index2==-1:
                index2=len(p)
            return p[:index2],p[index2:]
        if normp[1:2]==colon:
            return p[:2],p[2:]
    return p[:0],p





