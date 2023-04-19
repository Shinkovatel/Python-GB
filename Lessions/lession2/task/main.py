# list_1 = [1,5]
# print(list_1)
#
# list_1.append(8)
# print(list_1)
#
# list_1.append(5)
# print(list_1)

# list_1 = []
#
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# удаление последнего элемента
#
# list_2 = [12,7,-1,21,0]
#
# print(list_2.pop()) # удаляем последний элемент списка, 0
# print(list_2.pop()) # удаляем последний элемент списка, 21

# list_3 = [12,7,-1,21,0]
# print(list_3.pop(0)) # удаляем элемент с индексом 0, т.е. 12

# list_3 = [12,7,-1,21,0]
# print(list_3.insert(2,11)) # вставляем элемент по индексу 2, при этом элемент находившийся на этом месте ранее сдвигается на индекс 3
# print(list_3)

# Кортеж - неизменяемый список

# t = ()
# print(type(t))
#
# t = (1,)
# print(type(t))
#
# v =[1,3,5]
# print(v)
# print(type(v))
#
# v= tuple(v) # преобразование в кортеж
#
# print(v)
#
# a = 1
# b = 2
# # по другому
#
# a,b = 1,2
#
# a,b,c = v
#
# print(a, b, c)
#
# t = (1,3,5,6,)
#
# for i in t:
#     print(i)
#
# for i in range(len(t)):
#     print(t[i])
#
# t[0] = 2

# Словари неупорядочные коллекции произвольных объектов с доступом по ключу

# s = {}
#
# s = dict()
#
# s['q'] = 'qwerty'
# print(s)
#
# s['w'] = 'werty'
# print(s['q'])

# dictionary = {}
#
# dictionary = {'up':'|', 'left': '?' }
# print(dictionary)
# print(dictionary['left'])
#
# dictionary[895] = 98993
# print(dictionary)
#
# del dictionary['left']
#
# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))
#
# for (k,v) in dictionary.items():
#     print(k,v)
#     print(dictionary.items())

# множества содержат уникальные элементы, не обязательно упорядоченные

# colors = {'red', 'green', 'blue'}
#
# print(colors)
#
# colors.add('red')
# colors.add('gray')
# colors.remove('red') # удаление элемента
# colors.discard('red') # удаление элемента с проверкой наличия его

a = {1,2,3,6,8}
b = {2,4,5,7,9}

c = a.copy() # копирование множества
u = a.union(b) # объединения а во множестве б
i = a.intersection(b) # пересечение
dl = a.difference(b) # разность множества а по отношению к b берем множество а и вычитаем все из множества б {1,3,6,8}
dr = b.difference(a) # разность множества а по отношению к b берем множество b и вычитаем все из множества a {4,5,7,9}
q = a.union(b).difference(a.intersection(b))

print(i)
print(dl)
print(dr)
print(q)

a = {1,2,3}

b  = frozenset(a) # замороженное множество - неизменное

list = [i for i in range(1,100) if i % 2 == 0] # 2,4,6, ... 100

list_2 = [(i,i) for i in range(1, 100) if i % 2 == 0] # (2,2), (4,4) ... (100, 100)

list_3 = [i*2 for i in range(10) if i % 2 ==0] # [0,4,8,12,16]

