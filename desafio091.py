from time import sleep
from random import randint
from operator import itemgetter
resultados = {'jogador1': randint(1, 10), 
                'jogador2': randint(1, 10), 
                'jogador3': randint(1, 10), 
                'jogador4': randint(1, 10)}
print('Valores sorteados: ')
for chave, valor in resultados.items():
    print(f'{chave} tirou {valor}')
    sleep(1)
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True) #essa funçao vai englobar apenas os itens de indice 1, nesse exemplo

print('-' * 40)
print('Ranking: ')
for indice, valor in enumerate(ranking):
    print(f'{indice + 1}º lugar: {valor[0]} com {valor[1]}')
    sleep(1)