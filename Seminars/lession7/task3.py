def same_by (characteristic, objects)-> bool:
    return len(set(map(characteristic,objects))) <= 1

col = [2,4,8,22,14]

print(same_by(lambda x : x%2, col))

