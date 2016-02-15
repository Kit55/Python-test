class Reg:

	ex=[]

	def __init__(self):
		self.__class__.ex.append(self)#добавляем в список ex

	def __iter__(self):# при обращении как к итерируемому типу
		print ('%%%')
		return iter(self.__class__.ex)#возвращаем лист с классами


a=Reg()
b=Reg()
c=Reg()
d=Reg()

for i in Reg():
	print (i)
