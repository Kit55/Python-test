import itertools

def createGenerator(*_ars):
    """
    myit1=iter([1,2,3])
    myit2=iter([4,5,6])
    myit3=iter([7,8,9])
    myit4=iter([10,11,12])
    myit5=iter([13,14,15]) 
    
    mygenerator = createGenerator(myit1,myit2,myit3,myit4,myit5)

    for i in mygenerator:
    print (i)
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    """
    for g in _ars:
        for i in g:
            yield i

myit1=iter([1,2,3])
myit2=iter([4,5,6])
myit3=iter([7,8,9])
myit4=iter([10,11,12])
myit5=iter([13,14,15]) 

mygenerator = createGenerator(myit1,myit2,myit3,myit4,myit5)

for i in mygenerator:
    print (i)


if __name__ == "__main__":
    import doctest
    doctest.testmod()