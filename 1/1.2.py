#Как получить список всех публичных атрибутов объекта
a=dir(list) # а заносим атрибуты для типа list
for i in range (0,len(a)):
	if a[i].startswith("__"):
		print (a[i],end=' ')