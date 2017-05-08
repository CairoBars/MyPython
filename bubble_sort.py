from __future__ import print_function

def bubble_sort(ARRAY):
	ARRAY_LENGTH=len(ARRAY)
	for i in range(ARRAY_LENGTH-1,-1,-1):
		for j in range(i):
			if ARRAY[j+1]<ARRAY[j]:
				ARRAY[j],ARRAY[j+1]=ARRAY[j+1],ARRAY[j]


	return ARRAY


if __name__=='__main__':
	import sys
	if sys.version_info.major<3:
		input_function=raw_input
	else:
		input_function=input

	user_input= [int(element) for element in input_function('input number split by ,').split(',')]
	print(bubble_sort(user_input))
