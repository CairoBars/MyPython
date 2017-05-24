memo={0:0,1:1}

def fibm(n):
	if not n in memo:
		memo[n] = fibm(n-1)+fibm(n-2)
		print "GGGG"
	return memo[n]


fibm(5)



def pascal(n):
	if n==1:
		print [1]
		return [1]
	else:
		line=[1]
		previous_line=pascal(n-1)
		for i in range(len(previous_line)-1):
			line.append(previous_line[i]+previous_line[i+1])
		line+=[1]
		print line
	return line


#pascal(6)


def pascal_2(n):
	
	if n==1:
		line=[1]
		print line
		return line
	else:
		line=[1]
		previous_line=pascal_2(n-1)
		for i in range(n-2):
			line.append(previous_line[i+1]+previous_line[i])
		line.append(1)
		print line
		return line


pascal_2(6)