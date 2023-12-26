#from math import factorial  // usando módulo
#n = int(input('Digite um número para saber seu fatorial: '))
#f = factorial(n)  
#print(f'O fatorial de {n} é igual a {f}!')  

n = int(input('Digite um número para saber seu fatorial: '))
c = n
f = 1 #Fator nulo de multiplicação é 1. De soma e subtração é 0
while c > 0:
    print(f'{c}',end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1 #para TIRAR um do c
print(f'{f}')