"""
magicicans=['alice','david','carolina']
for magicican in magicicans:
	print(magicican.title()+", that was a great trick!")
	print("I can't wait to see your next trick, "+magicican.title()+".\n")
"""

"""
squares=[]
for value in range(1,11):
	squares.append(value*value)
print(squares) 
"""

"""
digit=[1,2,3,4,5,6,7,8,9]
print(min(digit))
print(max(digit))
print(sum(digit))
"""

#列表注释
squares=[value**2 for value in range(1,11)]
print(squares)


#切片
player=['charles','martina','michael','florence','eli']
print(player[0:3]) #输出索引0,1,2的数值
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())


#复制列表
my_foods=['cola','pizza','carrot','water']
friend_foods=my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("Friend favorite foods are:")
print(friend_foods)
my_foods.pop()
print(friend_foods)

#不可变的列表：元组
#dimensions=(200,20)

age0=22
age1=33
result0=age0>=23 and age1<=55
result1=age0<=22 and age0>=22


reqested_topping=['mushroom','onion','pineapple']
result2='mushroom' in reqested_topping
if 'gg' not in reqested_topping:
	print("Wa ha ha ha!")


#确定列表不是空
request_gg=[]
if reqested_gg:

available_topping=['mushroom','olives','green peppers','pepperoni']
request_toppings=['mushroom','french fries']

for element in reqested_toppings:
	if element in available_topping:
		print()
	else:
		print()



#字典
alien_0{'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])

#添加键值对
alien_0['ggsimida']='ggsimida'

#删除键值对
del alien_0['points']

#遍历字典
user_0={
	'username':'efermi',
	'first':'enrico',
	'last':'fermi'
}

for key,value in user_0.items():
	print("\nKey:"+key)
	print("value: "+value)

#按顺序遍历字典中的键或值
favorite_languag={
	'jen':'python',
	'sarach':'c',
	'edward':'ruby',
	'phil':'python',
}

for name in sorted(favorite_languag.keys()):
	print()

for value in sorted(favorite_languag.values()):
	print()

#提取值，如果要取消重复的值，可以用到set
for language in set(favorite_languag.values()):
	print()

#各种嵌套

alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}

aliens={alien_0,alien_1,alien_2}

for alien in aliens:
	print(alien)


#创建多个外星人对象防到一个列表中
#attri的定义放在循环内和循环外有什么不同呢？
 different=[]
 attri={
 	'color':'red',
 	'tall':20,
 	'shape':'square'
 }
 for g in range(30):
 	different.append(attri)


 #字典中存储列表信息
 pizza={
 	'crust':'thick',
 	'toppings':['mushroom','extra cheese'],
 }

#在字典中存储字典
users={
	'mouse':{
		'name':'tom'
	}
	'cat':{
		'name':'ruby'
	}
}

for username , userinfo in users.items():
	print('\nUsername: '+username)
	full_name=user_info['name']


#使用函数input()时，Python将用户输入解读为字符串。
height=input("How tall are you , in inches?")
height=int(height)
if(height>=35):
	print()


'''
如果使用Python2.7 ，应使用函数raw_input()来提示用户输入。这个函数与Python3中的input一样，也将输入解读为字符串
Python2.7也包含函数input(),但它将用户输入解读为Python代码，并尝试运行他们。
'''

#循环while
while True:
	city=raw_input()
	if city=='china':
		break
	else:
		continue

#使用while循环来处理列表
unconfirmed_users=['alice','brian','candance']
confirmed_user=[]

while unconfirmed_users:
	content_user=unconfirmed_users.pop()
	print("Verifying user:"+confirmed_user.title())
	confirmed_user.append(content_user)

pets=['dog','cat','dog','goldfish','cat','rabbit']
print(pets)

while 'cat' in pets:
	pets.remove('cat')


def make_pizza(*toppings):
	"""打印顾客点的所有配料"""
	"""形参名*toppings中的星号会让Python创建一个名为toppings的空元组"""
	print(toppings)


def build_profile(**user_info):
	"""形参**user_info是让Python创建一个名为user_info的空字典，并将受到的所有名称--键值对都封装到这个字典中
	print()






