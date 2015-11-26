def decwp(*_ars):
	def dec1(_fn):
		def dec2(*_ars2):
			#print (_ars,_ars2)
			if (len(_ars)!=len(_ars2)):
				print ("decwp1 not ok:(")
				return False
			for i in range (0,len(_ars)):
				if _ars[i]!=type(_ars2[i]):
					print ("decwp1 not ok:(")
					return False
			print ("decwp1 OK!")
			return True
		return dec2
	return dec1

def decwp2(_ars):
	def dec1(_fn):
		def dec2(*_ars2):
			b=_fn(_ars2)
			print (type(b))
			if (type(b)!=_ars): print ("decwp2 not ok:(")
			else:
				print ("decwp2 OK!")
			return True
		return dec2
	return dec1


@decwp(int,float)
def somef(*_ars):
	a=0
	for i in range(0,len(_ars)):
		a+=_ars[i]
	return type(a)

somef (1,2.5)
somef (2.5,3.5)
somef (6,1.5,6)

@decwp2 (int)
def somef(*_ars):
	a=0
	print (_ars)
	for i in range(0,len(_ars[0])):
		print (type (_ars[0][i]))
	return type(a)

somef (1,1)
somef (1,1.5)