different=[]

'''
attri={
	'gg':'gg',
	'33':'ff'
}
'''

for g in range(10):
	attri={
	'gg':'gg',
	'33':'ff'
	}
	different.append(attri)


different[0]['gg']='bb'
#attri['gg']='bb'
print(different)
