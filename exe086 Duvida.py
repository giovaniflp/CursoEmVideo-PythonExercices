lista_matriz = [[[],[],[]],
                [[],[],[]],
                [[],[],[]]]


contador = 0

for num in range(9):
    numero = int(input('Insira aqui seu número: '))
    if contador >= 0 and contador <= 2: #0 1 2
        lista_matriz[0][contador].append(numero)
    elif contador > 2 and contador <= 5: #3 4 5
        lista_matriz[1][contador].append(numero)
    elif contador >= 6: #6 7 8
        lista_matriz[2][contador].append(numero)
    contador = contador + 1
    

f323342


print (lista_matriz[0])
print (lista_matriz[1])
print (lista_matriz[2])

#DUVIDA
