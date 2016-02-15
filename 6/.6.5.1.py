class Node():
	l=None#левый потомок
	r=None#правый потомок
	p=None#родитель
	pl=None#правый или левый потомок относительно родителя
	lvl=0#глубина
	def __init__(self,_value):
		self.value=_value

	def __str__(self):
		return str(self.value)

	def aboutNode(self):
		print ('Нода '+str(self.value)+'. Родиетль '+str(self.p)+'. Правый потомок '+str(self.r)+'. Левый потомок '+str(self.l)+' Относительно родителя нода находится '+str(self.pl)+' Уровень='+str(self.lvl))



class tree():
	count=0
	def __init__(self,_node):
		self.root=_node
		self.count+=1
		print ('Создано дерево с конем '+str(self.root))

def insertNode(_tree,_node):
		passnod=_tree.root
		lvl=1
		while 1:
			if _node.value>passnod.value:#сравнение с текущей нодой
				if passnod.r:#проверка на существование правой (большей) ноды
					passnod=passnod.r
					lvl+=1
				else:
					print ('Нода '+str(_node.value)+' добавлена вправо. Родитель '+str(passnod.value))
					passnod.r=_node
					passnod.r.p=passnod
					passnod.r.pl='r'
					passnod.r.lvl=lvl
					_tree.count+=1
					break
			else:
				if _node.value<passnod.value:#сравнение с текущей нодой
					if passnod.l:#проверка на существование левой (меньшей) ноды
						passnod=passnod.l
						lvl+=1
					else:
						print ('Нода '+str(_node.value)+' добавлена влево. Родитель '+str(passnod.value))
						passnod.l=_node
						passnod.l.p=passnod
						passnod.l.pl='l'
						passnod.l.lvl=lvl
						_tree.count+=1
						break

				else:
					print ("Нода существует")
					break

def printTree(_tree):
	passnod=_tree.root
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
					if stack.pop()==_tree.root.value:#достаём из стека, но если это корень, то завершаем цикл
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
		#print ('check')
		if passnod==_tree.root:#если нет родителя. т.е мы перешли из того состояния когда из стека ДОСТАЛИ!! значение корня, обход завершен
			#print ('Родителя у элемента '+str(passnod)+' нет. Поиск завершен')
			break

def findNode(_tree,_value):
	passnod=_tree.root

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
					#print ('Нода '+str(_value)+' не найдена:(')
					return None

def findMax(_node):
	print('Поиск ноды')
	passnod=_node
	while not passnod.r:
		if passnod.l:
			passnod=passnod.l
		else:
			break
	while passnod.r:
		if passnod.r:
			passnod=passnod.r
		else:
			break
	print ('Максимальная нода='+str(passnod.value))
	return (passnod)

def delNode(_tree,_node):
	if _node:
		passnod=_node
		if not passnod.r and not passnod.l:#нет потомков
				print ('Удаление без детей')
				passnode=_node
				if passnode.p:
					if passnode.pl=='r':
						passnode=passnode.p
						passnode.r=None
					else:
						passnode=passnode.p
						passnode.l=None
				print ('Нода '+str(_node.value)+' удалена')
				return _node
		else:
			if (passnod.r or passnod.l) and  not(passnod.r and passnod.l):#имеется только 1 потомок
				print ('Удаление 1 ребенка')
				passnode=_node
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
				print ('Нода '+str(_node.value)+' удалена')
				return _node
			else:
				print ('Удаление 2 ребенка')
				passnode=findMax(_node.l)
				passnode=delNode(a, passnode)
				passnode.l=_node.l
				passnode.r=_node.r
				passnode.p=_node.p
				passnode.pl=_node.pl
				passnode.lvl=_node.lvl
				if passnode.r:
					passnode.r.p=passnode
				if passnode.l:
					passnode.l.p=passnode
				if _node.p:
					if _node.pl=='r':
						_node.p.r=passnode
					else:
						_node.p.l=passnode
				if not _node.p:
					_tree.root=passnode
				print ('Нода '+str(_node.value)+' удалена')

	else:
		print ('Нечего удалять')




def delNoChild(_tree,_node):
	print ('Удаление без детей')
	passnode=_node
	if passnode.p:
		if passnode.pl=='r':
			passnode=passnode.p
			passnode.r=None
		else:
			passnode=passnode.p
			passnode.l=None
	print ('Нода '+str(_node.value)+' удалена')
	return _node

def delOneChild(_tree,_node):
	print ('Удаление 1 ребенка')
	passnode=_node
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
	print ('Нода '+str(_node.value)+' удалена')
	return _node

def delTwoChild(_tree,_node):
	print ('Удаление 2 ребенка')
	passnode=findMax(_node.l)
	if passnode.r or passnode.l:
		passnode=delOneChild(_tree, passnode)
	else:
		passnode=delNoChild(_tree, passnode)
	passnode.l=_node.l
	passnode.r=_node.r
	passnode.p=_node.p
	passnode.pl=_node.pl
	passnode.lvl=_node.lvl
	if passnode.r:
		passnode.r.p=passnode
	if passnode.l:
		passnode.l.p=passnode
	if _node.p:
		if _node.pl=='r':
			_node.p.r=passnode
		else:
			_node.p.l=passnode





a=tree(Node(100))

insertNode(a, Node(50))
insertNode(a, Node(200))
insertNode(a, Node(25))
insertNode(a, Node(75))
insertNode(a, Node(80))
insertNode(a, Node(90))
insertNode(a, Node(30))
insertNode(a, Node(35))
insertNode(a, Node(31))
insertNode(a, Node(32))
insertNode(a, Node(24))
insertNode(a, Node(23))
insertNode(a, Node(21))
insertNode(a, Node(22))
insertNode(a, Node(300))
insertNode(a, Node(250))
insertNode(a, Node(150))
insertNode(a, Node(140))
insertNode(a, Node(160))
insertNode(a, Node(91))
insertNode(a, Node(89))

printTree(a)
findNode(a,100).aboutNode()
findNode(a,25).aboutNode()
findNode(a,75).aboutNode()
findNode(a,35).aboutNode()
delNode(a, findNode(a,100))
#findNode(a,100).aboutNode()
findNode(a,25).aboutNode()
findNode(a,75).aboutNode()
findNode(a,35).aboutNode()
printTree(a)
print (a.root.value)





