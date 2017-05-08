from __future__ import print_function

def selection_sort(collection):

	length=len(collection)
	for i in range(length):
		least=i
		for k in range(i+1,length):
			if collection[k]<collection[least]:
				least=k


		collection[least],collection[i]=(collection[i],collection[least])
		

	return collection


if __name__=='__main__':
	import sys
	if sys.version_info.major<3:
		input_function=raw_input
	else:
		input_function=input

	user_input=input_function('input you number seperated a comma:\n')
	unsorted=[int(element) for element in user_input.split(',')]
	print(selection_sort(unsorted))