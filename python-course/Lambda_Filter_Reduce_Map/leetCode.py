#_*_ coding:utf-8 _*_
def getSubstring(str):
	"""Longest Substring Without Repeating Characters"""
	resultStr=[]
	tempStr=""
	for i in range(len(str)-1):
		#result[a]=a in result and result[a]+1 or 1
		tempStr=str[i]
		for b in str[i+1:]:
			if b in tempStr:
				break
			else: tempStr+=b

		resultStr.append(tempStr)
	return sorted(resultStr,key=lambda x:len(x),reverse=True)[0]
	



def Median(lst1,lst2):
	"""Midian of Two Sorted Arrays"""
	#The overall run time complexity should be O(log(m+n))
	lst=sorted(lst1+lst2)
	isOdd=len(lst)%2
	temp=None
	if isOdd:
		return lst[len(lst)/2]
	else:
		twoSum=(lst[len(lst)/2]+lst[len(lst)/2-1])/float(2)
		return twoSum


def Palindromic(astr):
	"""获取最长回文字符串：从左读跟从右读一样的字符串"""
	if len(astr)<=1:
		return astr
	bstr=astr[::-1]
	length=len(astr)
	for num in range(length-1):
		for i in range(num+1):
			if astr[num-i:length-i]==bstr[i:length-num+i]:
				resultStr=astr[num-i:length-i]
				return resultStr


	return astr[0]








"""

n:[0:n]

n-1:[1,n] [0,n-1]

n-2:[2,n],[1,n-1],[0,n-2]

n-3:[3,n],[2,n-1],[1,n-2],[0,n-3]
"""


				
"""
	'abcde'
	abcde [0:5]	 abcd[0:4]  abc[0:3] ab[0:2]
	bcde  [1:5]  bcd[1:4]
	cde   [2:5]	 cd[2:4]
	de    [3:5]

	'edcba'
	 edcba[0:5]   dcba[1:5] 
	 edcb [0:4]	  dcb[1:4]
	 edc  [0:3]   dc[1:3]
	 ed   [0:2]

"""





Palindromic("babadabbdaabdaaae")