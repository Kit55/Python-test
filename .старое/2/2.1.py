
def myfunc (*_forsum):
    """
    >>> myfunc(1,2,(5,6,7,(1,2,3)),[10,20,30])
    87
    """
    sum=0
    for i in _forsum:
        if hasattr(i,  '__iter__'):
            sum+=myfunc(*i)
        else:
            sum+=i
    return sum

print (myfunc(1,2,(5,6,7,(1,2,3)),[10,20,30]))

if __name__ == "__main__":
    import doctest
    doctest.testmod()

