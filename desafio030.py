n = int(input('Digite um número qualquer: '))
num = n % 2
#qualquer numero par dividido por 2 vai ter resto 0, e os ímpares vão ter resto 1
if num == 0:
    print('O número {} é PAR'.format(n))
else:
    print('O número {} é ÍMPAR'.format(n))