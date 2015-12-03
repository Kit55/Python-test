import time

def timecount_decor(_somef):
	def timecount_decor_wrap(*_arr):
		st=time.clock()
		result=_somef(*_arr)
		ed=time.clock()
		print ("Время выполнения функции=",ed-st)
		return result
	return timecount_decor_wrap

@timecount_decor
def countx():
	for i in range (0,100000):
		for g in range (0,1000):
			a=i+g
	return (a)

countx()


