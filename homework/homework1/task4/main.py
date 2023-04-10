sliceRow = int(input('введите высоту шоколадки в дольках : ')) 
sliceColumn = int(input('введите ширину шоколадки в дольках : '))
matrix = sliceColumn * sliceRow # считаем размер шоколадки

fault = int(input('сколько долек хотите отломать :'))
        
if (fault % sliceColumn == 0) and fault < matrix: # проверяем что отламываемая долька кратна ширине и меньше чем вся шоколадка
    print('Можно отломать без проблем')
elif fault == matrix:
    print('Тут нечего ломать')
elif fault > matrix:
    print('Нельзя отломать больше чем целая шоколадка')
else:    
    print('Ровно не отломать Придеться брать нож :)')

    