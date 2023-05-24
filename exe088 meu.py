import random

lista = []

jogos = int(input('Quantos jogos serão gerados? '))

aleatorizar = jogos

for num in range(6):
    lista.append(random.randint(0,60))
    for num in jogos:
        lista.extend()

print(lista)