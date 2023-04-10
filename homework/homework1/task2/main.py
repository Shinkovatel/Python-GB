import math
CraneSum = int(input('введите общее количество журавликов: '))

Point = CraneSum / 6
Serg = math.ceil(Point)

Petya = Serg

Kate = math.floor(Point * 4)

print(f"Петя сделал {Petya} журавликов, Сергей сделал {Serg} журавликов, Катя сделала {Kate} журавликов")

