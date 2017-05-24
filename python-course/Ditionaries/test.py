

def my_sort(list):
	result={}
	for a  in list:
		result[a]=(a not in result and 1 or result[a]+1)


	result2=sorted(result.iteritems(),key=lambda x:x[1],reverse=True)

	result2=[a[1] for a in result2]

	print result2


def my_sort_2():
	a=2
	result={'a':2,2:3}
	result[a]+=1
	print(result['a'])
	print(result[2])


def test_lambda(lst):
	print map(lambda x:x+1,lst)
	print filter(lambda x:x%2==0,lst)
	print reduce(lambda x,y:x*y,lst)




if __name__=='__main__':
	my_sort([1,2,3,2,3,1,2,2])
	test_lambda([1,2,3,4,5])
	#my_sort([1,2,3,2,3,1,2,2])
	#my_sort_2()
	#my_sort_3({2:3,3:1,1:4})

		



