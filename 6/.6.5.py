class Node():
	l=None
	r=None
	p=None
	def __init__(self,_value):
		self.value=_value

	def __str__(self):
		return str(self.value)

	def aboutNode(self):
		print ('Нода '+str(self.value)+'. Родиетль '+str(self.p)+'. Правый предок '+str(self.r)+'. Левый предок '+str(self.l))



class tree():
	def __init__(self,_node):
		self.root=_node
		print ('Создано дерево с конем '+str(self.root))

	def insertNode(self,_node):
		passnod=self.root
		while 1:
			if _node.value>passnod.value:#сравнение с текущей нодой
				if passnod.r:#проверка на существование правой (большей) ноды
					passnod=passnod.r
				else:
					print ('Нода '+str(_node.value)+' добавлена вправо. Родитель '+str(passnod.value))
					passnod.r=_node
					passnod.r.p=passnod
					break
			else:
				if _node.value<passnod.value:#сравнение с текущей нодой
					if passnod.l:#проверка на существование левой (меньшей) ноды
						passnod=passnod.l
					else:
						print ('Нода '+str(_node.value)+' добавлена влево. Родитель '+str(passnod.value))
						passnod.l=_node
						passnod.l.p=passnod
						break

				else:
					print ("Нода существует")
					break

	def printTree(self):
		passnod=self.root
		stack=[None]

		while 1:#основной цикл, крутится пока есть родители
			#print ('Основной цикл:')
			while passnod.l:#поиск крайнего левого
				passnod=passnod.l
			
			while 1:
				#print ('Внутренний цикл:')
				if passnod.r and stack[len(stack)-1]!=passnod.value:#если существует правый предок и последний элемент стека не равняется текущему
					#print ('Есть потомок '+str(passnod.r)+' последнее значение стека '+str(stack[len(stack)-1])+' не равно значению текущего элемента '+str(passnod.value))
					stack.append(passnod.value)#заносим в стек, выводим и уходим к правому потомку
					#print ('Заносим в стек '+str(passnod.value))
					print (passnod)
					passnod=passnod.r
					#print ('Переходим на право к значению'+str(passnod.value)+' уходим искать левое значение')
					break#ищем левое значение
				else:
					if passnod.value==stack[len(stack)-1]:#если правое существует, но значение текущего равно последнему элементу стека
						#print ('Последнее значение стека '+str(stack[len(stack)-1])+' равно значению текущего элемента '+str(passnod.value))
						if stack.pop()==self.root.value:#достаём из стека, но если это корень, то завершаем цикл
							#print ('Корень найден')
							break
						#print ('Достаём значение из стека, новое последнее значение ='+str(stack[len(stack)-1]))
						passnod=passnod.p
					else:
							#print ('Печать значения перед переходом к родителю:')
						print (passnod)
						if passnod.p:
							passnod=passnod.p#переходим к родителю
							#print ('Переходим к родителю '+str(passnod))
						else:
							break
			if not passnod.p:#если нет родителя. т.е мы перешли из того состояния когда из стека ДОСТАЛИ!! значение корня, обход завершен
				#print ('Родителя нет у элемента '+str(passnod)+' нет. Поиск завершен')
				break

	def findNode(self,_value):
		passnod=self.root

		while 1:
			if _value>passnod.value and passnod.r:
				passnod=passnod.r
			else:
				if _value<passnod.value and passnod.l:
					passnod=passnod.l
				else:
					if _value==passnod.value:
						print ('Нода '+str(_value)+' найдена!')
						return passnod
					else:
						print ('Нода '+str(_value)+' не найдена:(')
						return None

	def delNode(self,_node):
		if _node:
			passnod=_node
			if not passnod.r and not passnod.l and passnod.p:
				if passnod.p.r.value==passnod.value:
					passnod.p.r=None
				else:
					passnod.p.l=None
			else:
				if passnod.r or passnod.l and passnod.p:
					print ('Нода '+str(passnod.value)+' удалена')
		else:
			print ('Нечего удалять')



a=tree(Node(100))


a.printTree()

a.findNode(21)

a.delNode(a.findNode(15))

a.printTree()