class DictAttr(dict):#наследуем от словаря
	"""
	>>> x=DictAttr({'one':1,'two':2,'three':3})
	>>> print (x['three'])
	3
	>>> print (x.get('one'))
	1
	>>> print (x.get('five', 'missing'))
	missing
	>>> print (x.one)
	1
	>>> print (x.five)
	Error
	"""
	def __getattr__(self, _attr):#выполняется когда мы патаемся обратиться к атрибуту
		try:
			return self[_attr]
		except:
			return ("Error")

x=DictAttr({'one':1,'two':2,'three':3})
print (x['three'])
print (x.get('one'))
print (x.get('five', 'missing'))
print (x.one)
print (x.five)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
