#Есть два списка одинаковой длины, в одном ключи, в другом значения. Составить словарь.
dnames = ["name1","name2","name3","name4","name5","name6"]
dkeys = ["key1","key2","key3","key4","key5","key6"]
d = {dkeys[i]: dnames[i] for i in range(len(dnames))}
print (d)
