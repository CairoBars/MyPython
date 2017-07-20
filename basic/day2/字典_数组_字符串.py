import copy

#Author:Cairo Li
bigbooks=['西游记','水浒传','三国演义','红楼梦']

copybooks=bigbooks[:]  #浅拷贝
copybooks=copy.copy(bigbooks) #浅拷贝
copybooks=copy.deepcopy(bigbooks)#深拷贝

#追加
bigbooks.append('西厢记')
#插入
bigbooks.insert(2,'宋词')
#删除
bigbooks.remove('宋词')
bigbooks.pop() #删除最有一个
del bigbooks[4]
#扩展
bigbooks2=["史记",'葵花宝典']
bigbooks.extend(bigbooks2)

#拷贝
copybooks=bigbooks.copy() #浅拷贝

#统计
bigbooks.append('宋词')
bigbooks.append('宋词')
bigbooks.append('宋词')
bigbooks.count('宋词')

#排序
names=['dewa','diediedie','mouse',2,3,4]
names.sort()#这里会报错，在PY3中不同类型不能排序
names.reverse()#反转

#获取下标
index=bigbooks.index('红楼梦')

#元组，其实跟列表差不多，不过一旦创建就不能修改，所以只有count,index两个方法
names2=('a','b','c')
names2.count('a')
names2.index('a')




