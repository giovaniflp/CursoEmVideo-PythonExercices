import itertools

lista = []
lista_pares = []
lista_impares = []

for num in itertools.count():
    numeros = int(input('Digite aqui seus números(Para sair digite: 999): '))
    if numeros == 999:
        break
    lista.append(numeros)

print(lista)

for num in lista:
    if num %2==0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)

print(lista_pares)
print(lista_impares)