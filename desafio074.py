from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), 
    randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram {n}')
#Metodo para achar maior e menor valor dentro das tuplas.
print(f'O maior valor sorteado foi {max(n)} e o menor foi {min(n)}')

#corrigido