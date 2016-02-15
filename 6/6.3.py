class XDictAttr(dict):
	"""
	>>> x=X({'one':1,'two':2,'three':3})
	>>> print (x['three'])
	3
	>>> print (x.get('one'))
	1
	>>> print (x.get('five', 'error'))
	error
	>>> print (x.one)
	1
	>>> print (x['return5'])
	5
	>>> print (x.return9)
	9
	>>> print (x.get('return15', 'error'))
	error
	"""
	def __getattr__(self, _attr):

		for attr in dir(self):#ищем методы которые начинаются с get_ и сохраняем их как словарь
			if callable(getattr(self,attr))and attr.startswith( 'get_' ):
				self.update({attr[4:]:getattr(self,attr)()})
				
		try:
			return self[_attr]
		except:
			return ("Error")

class X(XDictAttr):
	def get_return5(self):
		return 5

	def get_return12 (self):
		return 12

	def get_return9(self):
		return 9
	
x=X({'one':1,'two':2,'three':3})
print (x['three'])
print (x.get('one'))
print (x.get('five', 'error'))
print (x.one)
print (x['return5'])
print (x.return9)
print (x.get('return15', 'error'))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
