import random
from time import sleep

n = int(input('''Suas opções:
Digite 1 para PEDRA
Digite 2 para PAPEL
Digite 3 para TESOURA
Sua jogada: '''))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

if n == 1:
    j = 'PEDRA'
elif n == 2:
    j = 'PAPEL'
elif n == 3:
    j = 'TESOURA'
a = ['PEDRA', 'PAPEL', 'TESOURA']
i = random.choice(a)
print(f'Você jogou {j}! O computador jogou {i}!')
if j == 'PEDRA' and i == 'TESOURA':
    print('Você ganhou!')
elif j == 'PAPEL' and i == 'PEDRA':
    print('Você ganhou!')
elif j == 'TESOURA' and i == 'PAPEL':
    print('Você ganhou!')
elif j == i:
    print('Empatou! Jogue novamente.')
else:
    print('O computador ganhou!')

