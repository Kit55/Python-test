#Есть словарь. Инвертировать его. Т.е. пары ключ: значение поменять местами — значение: ключ.
d={'key5': 'name5', 'key2': 'name2', 'key1': 'name1', 'key3': 'name3', 'key4': 'name4', 'key6': 'name6'}
d = {list(d.values())[i]:list(d.keys())[i] for i in range(len(d))}
print (d)