#Author:Cairo Li

def getName(n):
    """
    >>> getName(9)
    success
    >>> getName(-2)
    Traceback (most recent call last):
        ...
    ValueError: gg
    """

    if n>0:
        print("success")
    elif n<0:
        raise ValueError("gg")





if __name__=="__main__":
    import doctest
    doctest.testmod()