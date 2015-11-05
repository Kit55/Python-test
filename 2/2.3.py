#Написать фабрику, аналогичную п.2, но возвращающей список таких функций
def addit(_add):
    def hidden(_hid):
        return(_add+_hid)
    return hidden

def add_range(_start,_finish):
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
#Немного не так как в задании, но я подумал что смысл тот-же

