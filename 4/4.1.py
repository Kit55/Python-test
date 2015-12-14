import itertools

def createGenerator(_iter):
    """
    >>> myit=iter([1,2,3])
    >>> mygenerator = createGenerator(myit)
    >>> for i in range (0,6):
    >>>     mygenerator.__next__()
    1
    4
    9
    1
    4
    9
    """
    for i in itertools.cycle(_iter):
        yield i*i

myit=iter([1,2,3])
mygenerator = createGenerator(myit)
for i in range (0,6):
    print(mygenerator.__next__())


if __name__ == "__main__":
    import doctest
    doctest.testmod()