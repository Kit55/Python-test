import time


def timecount(_somef):
	def hid():
		st=time.clock()
		_somef()
		ed=time.clock()
		return (ed-st)
	return hid

@timecount
def countx():
	for i in range (0,100000):
		for g in range (0,1000):
			a=i+g
	return (a)

print (countx())
	
