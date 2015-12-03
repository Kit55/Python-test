#Как получить список методов объекта
a=dir(list) # а заносим атрибуты для типа list
for i in range (0,len(a)):
	if not a[i].startswith("_") and callable(getattr(a, a[i])): #getattr возвращает имя атрибута, getattr(a, 'remove')=a.remove, callable=1 если объект может быть вызван
		print (a[i],end=' ')