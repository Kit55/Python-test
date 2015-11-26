
def decor(_fn):
	def hid():
		print ("I'm was here!:)")
		return _fn
	return (hid())
	
@decor
def somefunc():
	return ("Hi")

help (somefunc)
