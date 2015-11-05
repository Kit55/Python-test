print ("1.1")
class NC():
	name = "Unknow"
	age = 0
	def fx(self):
		print(dir (self))

def sum(_x, _y):
	x=_x
	y=_y
	return x+y

obj1=NC()
obj1.fx() #получить список всех аргументов __*name*__-публичные, стандартные для объекта. 'age', 'fx', 'name']-мои.
print ("\n")
#*********************************************************
print ("1.2")
a=dir(obj1)

i=0
while i<len(a):#вывод публичных атрибутов т.е которые начнинаются с __
	if ( a[i][0]=='_' and a[i][1]=='_'):
		print (a[i],end=' ')
	i+=1
print ("\n")
#*********************************************************
#В Питоне поля и методы обычно называются общим термином атрибуты.
#*********************************************************
print ("1.3")
i=0
while i<len(a):#вывод методов
	if (callable(getattr(obj1, a[i]))and not a[i][0]=='_'):
		print (a[i])
	i+=1
print ("\n")
#*********************************************************
print ("1.4")
print (callable.__doc__) #содержимое help
print ("\n")
#*********************************************************
print ("1.5")
#Конкатенация— операция склеивания объектов линейной структуры, обычно строк. Например, конкатенация слов «микро» и «мир» даст слово «микромир».
def kont (_k1,_k2):
	return _k1+_k2
t1=(4,5,6)
t2=(5,10)
print (kont (t1,t2))
print ("\n")
#*********************************************************
print ("1.6")
t1=(0,1,2,3,4,5,6,7,8,9,10)
t2=(2,4,5,6,9)
l1=[]#пустой список
i=0
while i<len(t1):
	g=0
	while g<len(t2):
		if t1[i]==t2[g]:
			l1.append(t1[i])#если значение совпадает, добавляем элемент в список
		g+=1
	i+=1
t3=tuple(l1)#конвертируем список в кортеж
print (t3)
print ("\n")
#*********************************************************
print ("1.7")
s=[2,5,2,4,-5,16,-7,3]
for l in s[:]:#при использовании [:] создается ещё 1 список, в l заносятся значения из копии
	s.pop()
	print (l,end=",")
print ("\n")
print (s)# после выполнения список пуст т.к pop выполнилнился столько раз, сколько элементов в списке
print ("\n")
s=[2,5,2,4,-5,16,-7,3]
for l in s:#в l заносятя значения из списка s который меняется во время выполнения цикла, 4 элемента вывелось, 4 было удалено
	s.pop()
	print (l,end=",")
print ("\n")
#*********************************************************
print ("1.8")
dnames = ["name1","name2","name3","name4","name5","name6"]
dkeys = ["key1","key2","key3","key4","key5","key6"]
d = {dkeys[i]: dnames[i] for i in range(len(dnames))}
print (d)
print ("\n")
#*********************************************************
print ("1.9")
dnames = ["name1","name2","name3","name4","name5",]#Ключей больше
dkeys = ["key1","key2","key3","key4","key5","key6"]
if (len(dkeys)>len(dnames)):
	for i in range (len(dnames),len(dkeys)):
		dnames.append("None")
	d = {dkeys[i]: dnames[i] for i in range(len(dkeys))}
else:
	d = {dkeys[i]: dnames[i] for i in range(len(dkeys))}
print (d)

dnames = ["name1","name2","name3","name4","name5","name6"]#Значений больше
dkeys = ["key1","key2","key3","key4","key5"]
if (len(dkeys)>len(dnames)):
	for i in range (len(dnames),len(dkeys)):
		dnames.append("None")
	d = {dkeys[i]: dnames[i] for i in range(len(dkeys))}
else:
	d = {dkeys[i]: dnames[i] for i in range(len(dkeys))}
print (d)
print ("\n")
#*********************************************************
print ("1.10")
d={'key5': 'name5', 'key2': 'name2', 'key1': 'name1', 'key3': 'name3', 'key4': 'name4', 'key6': 'name6'}
d = {list(d.values())[i]:list(d.keys())[i] for i in range(len(d))}
print (d)
print ("\n")
#*********************************************************
print ("1.11")
a=u'Hello world'
print (a)
print (a.encode(encoding="UTF-8"))
print (a.encode(encoding="cp1251"))
print ("\n")
#*********************************************************
print ("1.12")
a=a.encode(encoding="cp1251")
print (a)
print (a.decode("cp1251"))
