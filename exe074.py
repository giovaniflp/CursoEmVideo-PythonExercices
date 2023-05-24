import random

list = []

for num in range(5):
    list.append(random.randint(0,9))

tuple01 = tuple(list)



print(f'A tupla: {tuple01}, Menor valor: {min(tuple01)}, Maior valor: {max(tuple01)}')
    