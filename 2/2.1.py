#Написать функцию, которой можно передавать аргументы либо списком/кортежем, либо по одному. Функция производит суммирование всех аргументов.
def myfunc (*_forsum):
    sum=0
    print (_forsum)
    for i in _forsum:
        if type(i)==tuple or type(i)==list:
            for g in i:
                sum+=g
        else:
            sum+=i
    return sum
print (myfunc(1,2,(5,6,7),[10,20,30]))
