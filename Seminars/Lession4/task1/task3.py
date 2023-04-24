# m = 1
# max_number = -1
# while m != 0:
#     if m > max_number:
#         max_number = m
#     m = int(input('введите число '))
# print(max_number if max_number != -1 else 'вы нечего не ввели')


rus_letters = rus_lowers = rus_uppers = ''

for i in range(1040, 1104):
    rus_letters += chr(i)

for i in range(1040, 1072):
    rus_uppers += chr(i)

for i in range(1072, 1104):
    rus_lowers += chr(i)


print(rus_letters + chr(1025) + chr(1105))
print(rus_uppers + chr(1025))
print(rus_lowers + chr(1105))