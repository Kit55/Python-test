#Есть строка в юникоде, получить 8-битную строку в кодировке utf-8 и cp1251
a=u'Hello world'
print (a)
print (a.encode(encoding="UTF-8"))
print (a.encode(encoding="cp1251"))