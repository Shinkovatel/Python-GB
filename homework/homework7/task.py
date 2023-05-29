def rifma (words):
    return sum(1 for i in words if i in 'аеёиуыэюя')

text = input('введите фразы: ')

words = text.lower().split()
text_1 = rifma(text[0])
if all([rifma(i) == text_1 for i in words]):
    print('Парам пам-пам')
else:
    print('Пам парам')

