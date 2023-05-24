import itertools

lista = []

for num in itertools.count():
    numeros = int(input('Digite aqui seus números(Para sair digite: 999): '))
    if numeros == 999:
        break
    lista.append(numeros)

print(f'Foram digitados {len(lista)} números.')
print(f'Aqui está a lista organizada: {sorted(lista, reverse=True)}') # type: ignore

if lista.count(5) > 0:
    print('O valor 5 foi digitado e está na lista.')
else:
    print('O valor 5 não foi encontrado e não está na lista.')