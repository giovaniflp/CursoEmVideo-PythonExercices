lista = []

for num in range(4):
    add = int(input('Insira aqui seus valores: '))
    lista.append(add)

tuple01 = tuple(lista)
print (f'Essa é a tupla: {tuple01}')

# Letra A
nove = tuple01.count(9)
print(f'Essa tupla possui {nove} nove(s)')

# Letra B
if tuple01.count(3) > 0:
    print(f'O primeiro número três foi digitado em: {tuple01.index(3)+1}° lugar')
else:
    print('Não foram identificados números três na tupla.')

# Letra C
num_list = []

for num in tuple01:
    if num % 2==0:
        num_list.append(num)
   
print(f'Os números pares são: {num_list}')
    