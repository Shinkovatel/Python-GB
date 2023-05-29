import random


def generator (count_of_orbits: int) -> list[tuple[int,int]]:
    result = [(random.randint(1, 10), random.randint(1,10)) for i in range(count_of_orbits)]
    return result

def find_long_orbit(list_of_orbits: list[tuple[int,int]]) -> tuple[int,int]:
    square = [(i, e[0]*e[1]) for i,e in enumerate(list_of_orbits) if e[0] != e[1]]
    max_square = max(square, key= lambda x: x[1])
    return list_of_orbits[max_square[0]]

orbits=generator(10)
print(orbits)

print(find_long_orbit(orbits))

# альтернативный вариант

num = int(input('Enter a number planets: '))
orbit = [((random.randint(1,10)),random.randint(1,10)) for _ in  range(num)]
print(f'the list: {orbit}')

ell_sg = lambda rad: 3.1415*rad[0]*rad[1]
orbits_sg = [ell_sg(orbit[i]) for i in range(len(orbit))]
print(orbit[max([(val,ind) for ind, val in enumerate[orbits_sg] if orbit[ind][0] != orbit[ind][1]])[1]])
