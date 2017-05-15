

favorite_language="     python   "

favorite_language=favorite_language.rstrip()  
favorite_language=favorite_language.lstrip()
favorite_language=favorite_language.rstrip()

print "Hello Python 2.7"

print("Hello Python 3")  """python3 必须要括号"""

age=23
message ="Happy"+age+"rd Birthday"
print(message)  """TypeError:can't convert 'int' objcet to str implicitly """
message ="Happy"+str(age)+"rd Birthday"

print(favorite_language.title()) #首字母大写

motorcycles=['honda','yamaha','suzuki']
motorcycles.append('ducati')
motorcycles.insert(2,'choufeng')
del motorcycles[0]

poped_motorcycle=motorcycles.pop() #删除并弹出末尾元素
poped_motorcycle=motorcycles.pop(2)


motorcycles.remove('honda') #根据值删除

motorcycles.sort()
motorcycles.sort(reverse=True)

print(sorted(motorcycles)) #临时排序，不改变原来的排序
print(motorcycles[-1]) #打印最后一个元素
 
magicicans=['alice','david','carolina']
for magicican in magicicans:
	print(magicican.title()+", that was a great trick!")
	print("I can't wait to see your next trick, "+magicican.title()+".\n")




number=list(range(1,6)) #创建数字列表
