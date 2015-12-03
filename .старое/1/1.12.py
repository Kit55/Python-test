#Есть строка в кодировке cp1251, получить юникодную строку
a='Hello world'
a=a.encode(encoding="cp1251")
print (a)
print (a.decode("cp1251"))