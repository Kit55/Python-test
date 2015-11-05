
def addit(_add):
    def hidden(_hid):
        return(_add+_hid)
    return hidden

def add_range(_start,_finish):
    for i in range (_start,_finish):
        globals()['add%d' %i] = addit(i)

add_range(0, 10)

#Написать аналог map: 
#******************************
def map2(*_ars):
    l0=list()
    l1=list()
    l2=list()
    if hasattr(_ars[0], '__len__'):
        l0=_ars[0]
    else:
        l0.append(_ars[0])
    if hasattr(_ars[1], '__len__'):
        l1=_ars[1]
    else:
        l1.append(_ars[1])
    return [ i(g) for i in l0 for g in l1]

print(map2(add0,1))
print(map2(add0,[1,2]))
print(map2([add0,add1],1))
print(map2([add0,add1],[1,2]))

