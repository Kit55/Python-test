def addit(_add):
    def hidden(_hid):
        return(_add+_hid)
    return hidden

def add_range(_start,_finish):
    """
    >>> add_range(0, 10)
    >>> print (add0(1))
    1
    >>> print (add1(1))
    2
    >>> print (add2(1))
    3
    >>> print (add3(1))
    4
    >>> print (add4(1))
    5
    >>> print (add5(1))
    6
    >>> print (add6(1))
    7
    >>> print (add7(1))
    8
    >>> print (add8(1))
    9
    >>> print (add9(1))
    10
    """
    for i in range (_start,_finish):
        globals()['add%d' %i] = addit(i)

add_range(0, 10)

print (add0(1))
print (add1(1))
print (add2(1))
print (add3(1))
print (add4(1))
print (add5(1))
print (add6(1))
print (add7(1))
print (add8(1))
print (add9(1))


if __name__ == "__main__":
	import doctest
	doctest.testmod()
