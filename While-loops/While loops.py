list1 = [8, 3, 4, 5, 6, 7, 9]

total = 0
item_nr=0
print(len(list1))
while item_nr < len(list1):
#for item in list1:
    total += list1[item_nr]
    print(item_nr)
    item_nr+=1

print(total)