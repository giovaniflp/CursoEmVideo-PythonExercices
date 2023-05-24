import itertools

nomes = []
pesos = []

for num in itertools.count():
    nome = str(input('Insira aqui o nome: '))
    peso = float(input('Insira aqui o peso: '))
    sair = input('Sair?: ')

    nomes.append(nome)
    pesos.append(peso)
    if sair.lower() == ('sair'):
        break
    if sair.lower() == ('sim'):
        break
    else:
        continue

print(f'{len(nomes)} foram cadastradas.')
491fajfnja
