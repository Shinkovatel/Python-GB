import random

# list1 = [random.randint(1,9) for _ in range(10)]
# list2 = [random.randint(1,9) for _ in range(10)]
#
# print(list1)
# print(list2)
#
# list3 = []
#
# for i in list1:
#     if i not in list2:
#        list3.append(i) # в список значения можно добавить лишь через append
#
# print(list3)

# вариант препода
#
# list_1 = [random.randint(1,9) for _ in range(10)]
# list_2 = [random.randint(1,9) for _ in range(10)]
#
# через моржовый оператор
print(list_1 := [random.randint(0,10) for _ in range(10)])
print(list_2 := [random.randint(0,10) for _ in range(10)])
print(list_3 := [i for i in list_1 if i not in list_2])
# print(list_1)
# print(list_2)
#
# list_3 = [i for i in list_1 if i not in list_2]
#
# print(list_3)

# третий вариант через функции

def filling_list(number):
    return [random.randint(0,10) for i in range(number)]

def get_new_list(list_1,list_2):
    result = []
    for elem in list_1:
        if elem not in list_2:
            result.append(elem)
    return result

number_a = int(input('введите число элементов первого списка: '))
number_b = int(input('введите число элементов первого списка: '))

list11 = filling_list(number_a)
list12 = filling_list(number_b)

print(f'первый список {list11}')
print(f'второой список {list12}')

print(get_new_list(list11,list12))



