#Author:Cairo Li

def factorial(n):
    """
    Return the factorial of n ,an exact integer>=0
    >>[factorial(n) for n in range(6)]
    [1,1,2,6,24,120]




    """

    import math
    if not n>=0:
        raise ValueError("n must be >=0")
    if math.floor(n)!=n:
        raise ValueError("n must be exact integer")
    if n+1==n:  #catch a value lile le300
        raise OverflowError('n too large')
    result=1
    factor=2
    while factor<=n:
        result*=factor
        factor+=1
    return result

if __name__=="__main__":
    import doctest
    doctest.testmod()