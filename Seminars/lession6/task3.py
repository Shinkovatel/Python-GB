import random

print(my_list := [random.randint(0,9) for i in range(10)])

print(sum(my_list.count(i)//2 for i in set(my_list)))

# Можно перевести список в Sеt чтобы убрать дублирующие элементы далее по set пробегаем циклом


list1 = [random.randint(0,9) for i in range(10)]

count = 0

list2 = set(list1)

print(list1)
print(list2)

for i in list2:
    count += list1.count(i) // 2 # count(i) показывает сколько раз i элемент находится в данном списке

print(count)
