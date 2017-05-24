def reverse(x):

    numstr=str(x)
    if x<0:
        result=-int(numstr[::-1][0:len(numstr)-1])
        print result
        return judge(result)
    else:
        result=int(numstr[::-1])
        return judge(result)

def judge(x):
    if x<-2**31 or x >2**31-1:
        return 0
    else:
        return x
    

def regular_expression_matching():

    table=[[3]*5 for _ in range(3)]

    print table


regular_expression_matching()
