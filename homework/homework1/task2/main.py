import math
CraneSum = int(input('введите общее количество журавликов: '))

Serg = math.ceil(CraneSum / 6)

Petya = Serg

Kate = (Serg + Petya) * 2

print(f"Петя сделал {Petya} журавликов, Сергей сделал {Serg} журавликов, Катя сделала {Kate} журавликов")

