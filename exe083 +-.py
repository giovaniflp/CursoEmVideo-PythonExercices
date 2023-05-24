lista = []

palavra = str(input('Insira aqui sua palavra com parênteses: '))
lista.append(palavra)

for letra in palavra:
    if letra in '()':
        print('Possui parenteses')