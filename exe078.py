lista = []

for num in range(5):
    numeros = int(input('Insira aqui seus números: '))
    lista.append(numeros)

print(f'O maior valor foi: {max(lista)}, o menor valor foi: {min(lista)} e a posição respectivamente deles foi: {lista.index(max(lista))+1} e  {lista.index(min(lista))+1}')