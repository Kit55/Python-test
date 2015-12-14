
def addit(_add):
    def hidden(_hid):
        return(_add+_hid)
    return hidden

def add_range(_start,_finish):
    for i in range (_start,_finish):
        globals()['add%d' %i] = addit(i)

add_range(0, 10)

def map2(*_ars):
    """
    >>> map2([add0,add1],[1,2])
    [1, 2, 2, 3]
    """
    l0=list()
    l1=list()
    l3=list()
    if hasattr(_ars[0],  '__iter__'):
        l0=_ars[0]
    else:
        l0.append(_ars[0])
    if hasattr(_ars[1],  '__iter__'):
        l1=_ars[1]
    else:
        l1.append(_ars[1])
    for i in l0:
        l2=list()
        for g in l1:
            l2.append(i(g))
        l3.append(l2)
    return (l3)

print(map2(add0,1))
print(map2(add0,[1,2]))
print(map2([add0,add1],1))
print(map2([add0,add1],[1,2]))

tu=list(1)
tu+=1;

if __name__ == "__main__":
    import doctest
    doctest.testmod()