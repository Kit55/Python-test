def check_in_decor(*_ars):
	def check_in_decor_fn(_fn):
		def check_in_decor_ars(*_ars2):
			if (len(_ars)!=len(_ars2)):
				print ("check_in_decor not ok:(")
				return (_fn(*_ars2))
			for i in range (0,len(_ars)):
				if _ars[i]!=type(_ars2[i]):
					print ("check_in_decor not ok:(")
					return (_fn(*_ars2))
			print ("check_in_decor OK!")
			return (_fn(*_ars2))
		return check_in_decor_ars
	return check_in_decor_fn

def check_out_decor(_ars):
	def check_out_decor_fn(_fn):
		def check_out_decor_ars(*_ars2):
			b=_fn(*_ars2)
			if (type(b)!=_ars): 
				print ("check_out_decor not ok:(")
			else:
				print ("check_out_decor OK!")
			return b
		return check_out_decor_ars
	return check_out_decor_fn

@check_in_decor(int,float)
@check_out_decor(int)
def somef(*_ars):
	a=0
	for i in range(0,len(_ars)):
		a=a+_ars[i]
	return a

print (somef (1,2.5))
print ("\n")
print (somef (1,2))
