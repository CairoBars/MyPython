#Author:Cairo Li
import json
import pickle
f=open('test.txt','r')

#data=json.loads(f.read())
#data=pickle.loads(f.read())

for line in f:
    print(json.loads(line))