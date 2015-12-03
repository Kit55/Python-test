#Есть два списка разной длины, в одном ключи, в другом значения. Составить словарь. 
#Для ключей, для которых нет значений использовать None в качестве значения. Значения, для которых нет ключей игнорировать.
dnames = ["name1","name2","name3","name4","name5",]#Ключей больше
dkeys = ["key1","key2","key3","key4","key5","key6","key7"]
if (len(dkeys)>len(dnames)):
	for i in range (len(dnames),len(dkeys)):
		dnames.append("None")
	d = {dkeys[i]: dnames[i] for i in range(len(dkeys))}
else:
	d = {dkeys[i]: dnames[i] for i in range(len(dkeys))}
print (d)

dnames = ["name1","name2","name3","name4","name5","name6"]#Значений больше
dkeys = ["key1","key2","key3","key4"]
if (len(dkeys)>len(dnames)):
	for i in range (len(dnames),len(dkeys)):
		dnames.append("None")
	d = {dkeys[i]: dnames[i] for i in range(len(dkeys))}
else:
	d = {dkeys[i]: dnames[i] for i in range(len(dkeys))}
print (d)