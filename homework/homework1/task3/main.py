Number = input('введите шестзначное число: ')

FirstPart = int(Number[0])+ int(Number[1])+ int(Number[2])
SecondPart = int(Number[3])+ int(Number[4])+ int(Number[5])

if FirstPart == SecondPart:
    print('число счастливое')
else:
    print('число несчатливое')
    