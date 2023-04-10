
# print(f"{a} - {b} - {c}")
# print("{} - {}".format(a,b))

print('введите первую строку') # вывод на следующей строке
a = input()
print(a)

b = input('введите второе число: ') # вывод в этой строке

print(a, '+', b, '=', a + b)
x = int(input('dd'))

a = 4.3344
c = 5.55555

print(round(a*b, 2)) # округление до 2 знаков после запятой.

# математические операторы

a += 2 # тоже самое что и a = a + 2
a -= 2 # тоже самое что и a = a - 2
a *= 2 # тоже самое что и a = a * 2
a /= 2 # тоже самое что и a = a / 2
a //= 2 # тоже самое что и a = a // 2 деление без остатка на 2
a % 2 # тоже самое что и a = a % 2 
a ** 2 # тоже самое что и a = a ** 2 возведение в степень 2

a = 1 > 4
print(a) # выводиться False

a = 1 < 4 and 5 > 2 # условие И
print(a) # выводиться True

a = 1 == 2 # оператор равества двух чисел
print(a)
a = 1 != 2 # 
print(a)

a = 'qwe'
b = 'qwe'

print (a==b) 

a = 1 < 3 < 5 < 10

print (a)


while i  < 5:
    if i == 3:
        break
    i += 1
else
    print('fdfd')
    print('gffg')
print(i)

n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0 # если остаток при делении числа n на i равен 0
    flag = False
    print(i)
else i > n // 2 # делитель числа не может превышать введенное число, деленное на 2   
    print(n)
    flag = False
i += 1

f = range(5) # 0,1,2,3,4    
f = range(2,5) # 2,3,4
f = range(0,-5) # ----
f = range(1,10,2) # 1- цифра начала, 10 - конечная, 2- шаг 1,3,5,7,9
f = range(100,0,-20) # 100,80,60,40,20

a = 'qwerty'

print(a[0])

for i in a:
    print (i)

line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "+"
    print(line)
    
text = 'Съешь еще этих мягких французких булок'
print(len(text)) # позволяет узнать размер строки
print('еще' in text) # Если слово в строке текст
print(text.lower()) # позволяет перевести все в нижний регистр
print(text.upper()) # позволяет перевести в верхний регистр
print(text.replace('еще', 'ЕЩЕ')) # изменение слова с одного на другое

text = 'Съешь еще этих мягких французких булок'
print(text[0])
print(text[1])
print(text[len(text)-1]) # вывод последнего символа
print(text[-5]) # вывод пятого символа справа
print(text[:])  # вывод целиком строки
print(text[:2]) # вывод первых двух символов
print(text[len(text)-2:]) # вывод последних двух символов
print(text[2:9]) #
print(text[6:-18]) #
print(text[0:len(text):6]) # от 0 до конца с шагом 6 
print(text[::6]) # тоже самое что и выше

text = text[2:9] + text[-5] + text[:2] # срез

