#Author:Cairo Li

import queue


q=queue.PriorityQueue()

q.put((-1,"chenronghua"))
q.put((3,"hanyang"))
q.put((10,"alex"))
q.put((6,"wangsen"))

print(dir(q))
print((q.get()))
print((q.get()))
print(q.get())
print(q.get())