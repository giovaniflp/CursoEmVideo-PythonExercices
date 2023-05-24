import random
for x in range(int(input('Némero de jogos: '))):
    print(f'Jogo {x+1}: {random.sample(range(1, 61), 6)}')