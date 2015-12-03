def addit(_add):
    """
    >>> add1=addit(1)
    >>> print (add1(2))
    3
    """
    def hidden(_hid):
        return(_add+_hid)
    return hidden

add5=addit(5)
print (add5(3))
add10=addit(10)
print (add10(5))

laddit = lambda _add: lambda _hid: _add+_hid
add100=laddit(100)
print(add100(50))

if __name__ == "__main__":
    import doctest
    doctest.testmod()

