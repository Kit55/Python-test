#Написать функцию-фабрику, которая будет возвращать функцию сложения с аргументом.
def addit(_add):
    def hidden(_hid):
        return(_add+_hid)
    return hidden

add5=addit(5)
print (add5(3))
add10=addit(10)
print (add10(5))
#Написать варианты с обычной "внутренней" и анонимной lambda-функцией.

laddit = lambda _add: lambda _hid: _add+_hid
add100=laddit(100)
print(add100(50))

