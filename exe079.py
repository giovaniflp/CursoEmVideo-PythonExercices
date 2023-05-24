import itertools
lista = []

for num in itertools.count():
    numeros = int(input('Digite aqui seus números(Para sair digite: 999): '))
    if numeros == 999:
        break
    lista.append(numeros)
    if lista.count(numeros) > 1:
        lista.remove(numeros) 
print(sorted(lista))