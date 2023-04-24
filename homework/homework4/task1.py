import random

quantity_sets_a = int(input('количество элементов 1-го множества: '))

quantity_sets_b = int(input('количество элементов 2-го множества: '))


sets_a = {random.randint(0, 30) for i in range(quantity_sets_a)}

sets_b = {random.randint(0, 30) for i in range(quantity_sets_b)}

sets_c = sets_a.union(sets_b)
print(sets_a)
print(sets_b)
print(sets_c)