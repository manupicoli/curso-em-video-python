from random import randint
from time import sleep 

def sorteia(lista):
    for numero in range(0, 5):
        num = randint(0, 10)
        lista.append(num)
        print(f'{num}', end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    print(f'A soma de todos os números pares na lista {lista} é {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)

#corrigido