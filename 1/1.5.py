#Есть два кортежа, получить третий как конкатенацию первых двух
#Конкатенация— операция склеивания объектов линейной структуры, обычно строк. Например, конкатенация слов «микро» и «мир» даст слово «микромир».
def kont (_k1,_k2):
	return _k1+_k2
t1=(4,5,6)
t2=(5,10)
print (kont (t1,t2))