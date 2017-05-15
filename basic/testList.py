data=['g','d','e','w','w']
data2=[2,2,2,2,2,2,2]
def changeOriginArray(data):
	data[0]='a'

def noChangeOriginArray(data):
	data[0]=1
#data2[:]表示创建列表的副本
if __name__=='__main__':
	changeOriginArray(data)
	print(data)
	noChangeOriginArray(data2[:])
	print(data2)