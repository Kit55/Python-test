def some_dec(_fn):
	print ("I am was here")
	def some_dec_wrap():

		return _fn()
	return some_dec_wrap

@some_dec
def somef():
	return 42

help (somef)
