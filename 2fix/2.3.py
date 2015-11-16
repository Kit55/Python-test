def addit(_add):
    def hidden(_hid):
        return(_add+_hid)
    return hidden

def add_range(_start,_finish):
    """
    >>> a=add_range(0, 10)
    >>> print (a[0](1))
    1
    >>> print (a[1](1))
    2
    >>> print (a[2](1))
    3
    >>> print (a[3](1))
    4
    >>> print (a[4](1))
    5
    >>> print (a[5](1))
    6
    >>> print (a[6](1))
    7
    >>> print (a[7](1))
    8
    >>> print (a[8](1))
    9
    >>> print (a[9](1))
    10
    """
    for i in range (_start,_finish):
        return [addit(i) for i in range (_start,_finish)]

a=add_range(0, 10)
print (a[0](1))
print (a[1](1))
print (a[2](1))
print (a[3](1))
print (a[4](1))
print (a[5](1))
print (a[6](1))
print (a[7](1))
print (a[8](1))
print (a[9](1))



if __name__ == "__main__":
	import doctest
	doctest.testmod()
