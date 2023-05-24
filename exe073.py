#Tabela do ano de 2021

times = ('Atlético-MG','Flamengo','Palmeiras','Fortaleza','Corinthians','Bragantino','Fluminense','América-MG','Atletico-GO','Santos','Ceará','Internacional','São Paulo','Athletico-PR','Cuiabá','Juventude','Grêmio','Bahia','Sport','Chapecoense')

print(f'Os primeiros 5 colocados foram:', times[0:5])
print(f'Os 4 últimos colocados foram:', times[-4:-1], times[-1])

lista = list(times)
lista_arrumada = sorted(lista)
times_tupla = tuple(lista_arrumada)

print(f'Tupla em ordem alfabética: {times_tupla}')
print(f'A posição da Chape é:',times.index('Chapecoense')+1)

