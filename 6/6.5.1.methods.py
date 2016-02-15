class Node():
	l=None#левый потомок
	r=None#правый потомок
	p=None#родитель
	pl=None#правый или левый потомок относительно родителя
	def __init__(self,_value):
		self.value=_value

	def __str__(self):
		return str(self.value)

	def aboutNode(self):
		print ('Нода '+str(self.value)+'. Родиетль '+str(self.p)+'. Правый потомок '+str(self.r)+'. Левый потомок '+str(self.l)+' Относительно родителя нода находится '+str(self.pl))



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
						passnod.r.pl='r'
						break
				else:
					if _node.value<passnod.value:#сравнение с текущей нодой
						if passnod.l:#проверка на существование левой (меньшей) ноды
							passnod=passnod.l
						else:
							print ('Нода '+str(_node.value)+' добавлена влево. Родитель '+str(passnod.value))
							passnod.l=_node
							passnod.l.p=passnod
							passnod.l.pl='l'
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
					print (passnod, end=' ')
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
						print (passnod, end=' ')
						if passnod.p:
							passnod=passnod.p#переходим к родителю
							#print ('Переходим к родителю '+str(passnod))
						else:
							break
			#print ('check')
			if passnod==self.root:#если нет родителя. т.е мы перешли из того состояния когда из стека ДОСТАЛИ!! значение корня, обход завершен
				#print ('Родителя у элемента '+str(passnod)+' нет. Поиск завершен')
				break
		print ('')

	def findNode(self,_value): #поиск элемента во всём дереве
		passnod=self.root

		while 1:
			if _value>passnod.value and passnod.r:
				passnod=passnod.r
			else:
				if _value<passnod.value and passnod.l:
					passnod=passnod.l
				else:
					if _value==passnod.value:
						#print ('Нода '+str(_value)+' найдена!')
						return passnod
					else:
						print ('Нода '+str(_value)+' не найдена:(')
						return None

	def findMax(self,_value):#поиск макс.ноды начиная с ноды со значением _value
		#print('Поиск макс ноды')
		passnod=self.findNode(_value)
		if passnod:
			if passnod.r:
				while passnod.r:
					passnod=passnod.r
			#print ('Максимальная нода='+str(passnod.value))
			return (passnod)
		else:
			print ("Ошибка при поиске максимального значения. Нет ноды для поиска")
			return None

	def delNode(self,_value):#удалене ноды, резделяется на 3 разных способа, по количесву потомков
		node=self.findNode(_value)
		if node:
			passnod=node
			if not passnod.r and not passnod.l:#нет потомков (не 0 и не 0)
					#print ('Удаление без детей')
					passnode=node
					if passnode.p:
						if passnode.pl=='r':
							passnode=passnode.p
							passnode.r=None
						else:
							passnode=passnode.p
							passnode.l=None
			else:
				if (passnod.r or passnod.l) and  not(passnod.r and passnod.l):#имеется только 1 потомок ((правый или левый) и не(правый и левый))
					#print ('Удаление 1 ребенка')
					passnode=node
					if passnode.l:
						passnode=passnode.l
					else:
						passnode=passnode.r
					passnode.pl=passnode.p.pl
					if passnode.p.pl=='r':
						passnode.p.p.r=passnode
					else:
						passnode.p.p.l=passnode
					passnode.p=passnode.p.p
				else:#если есть потомки и их не 1, значит 2
					#print ('Удаление 2 ребенка')
					passnode=self.findMax(node.l.value)#находим макс.значение в левом (меньшем) поддереве
					passnode=self.delNode(passnode.value)#удаляем его из поддерева и записываем в переменную
					passnode.l=node.l#копируем все ссылки от удаляемого элемента к заменяемому
					passnode.r=node.r
					passnode.p=node.p
					passnode.pl=node.pl
					if passnode.r:#если остался правый потомок, то у него изменяем ссылку на родителя
						passnode.r.p=passnode
					if passnode.l:#если остался левый потомок, то у него изменяем ссылку на родителя
						passnode.l.p=passnode
					if node.p:
						if node.pl=='r':
							node.p.r=passnode
						else:
							node.p.l=passnode
					if not node.p:#если у начального элемента небыло родителя, значит он был корнем
						self.root=passnode
			#print ('Нода '+str(node.value)+' удалена')
			return node
		else:
			print ('Ошибка при удалении. Нода не найдена')

a=tree(Node(100))
a.insertNode(Node(50))
a.insertNode(Node(200))
a.insertNode(Node(25))
a.insertNode(Node(75))
a.insertNode(Node(80))
a.insertNode(Node(90))
a.insertNode(Node(30))
a.insertNode(Node(35))
a.insertNode(Node(31))
a.insertNode(Node(32))
a.insertNode(Node(24))
a.insertNode(Node(23))
a.insertNode(Node(21))
a.insertNode(Node(22))
a.insertNode(Node(300))
a.insertNode(Node(250))
a.insertNode(Node(150))
a.insertNode(Node(140))
a.insertNode(Node(160))
a.insertNode(Node(91))
a.insertNode(Node(89))
a.printTree()

a.findNode(999)
a.findMax(999)
a.delNode(999)


a.findNode(25).aboutNode()

a.delNode(25)

a.findNode(50).aboutNode()
a.findNode(24).aboutNode()
a.findNode(30).aboutNode()

a.printTree()




