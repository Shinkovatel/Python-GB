import keyword

# my_list = [] # Список, изменяемый тип, может быть любой длинны, для любого типа данных
#
# my_tuple = () # Кортеж, неизменяемый тип, для любых типов данных,
#
# my_set = set() # Множество, коллекция
#
# my_dict = {} # Словарь
#
# print(keyword.kwlist) # Слова которые нельзя использовать как название переменных

# my_list = [1,2,3,2,4,3,5,5,6]
#
# my_set1 = set(my_list)
#
# print(my_set1)
#
# my_list1 = [i for i in range(10)]
# print(my_list1)
# shift = int(input('На сколько сдвигаем вправо'))
#
# for _ in range(shift):
#     my_list1.insert(0,my_list1.pop())
#
# print(my_list1)
#
# list =  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
# unigue_values = set()
# for element in list:
#     for value in element.values():
#         unigue_values.add(value)
# print(unigue_values)
#
# # Решение препода
#
# list1 =  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
#
# res = set()
#
# for i in list1:
#     for (k,v) in i.items():
#         res.add(v)
# print(res)
#
import random

numbers = [1,2,1,3,4,7,1,0,1]
count = 0

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        count += 1
print(count)

numbers1 = [random.randint(0,23) for i in range (24)]
