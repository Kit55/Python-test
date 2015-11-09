
def myfunc (*_forsum):
    """
    >>> myfunc(1,2,(5,6,7),[10,20,30])
    81
    """
    sum=0
    for i in _forsum:
        if type(i)==tuple or type(i)==list:
            for g in i:
                sum+=g
        else:
            sum+=i
    return sum
print (myfunc(1,2,(5,6,7),[10,20,30]))

if __name__ == "__main__":
    import doctest
    doctest.testmod()

