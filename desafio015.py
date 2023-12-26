d = int(input('Quantos dias você usou o carro? '))
k = int(input('Quantos km rodados? '))

p = 60 * d
p2 = 0.15 * k

t = p + p2

print('O preço total a pagar será {}'.format(t))

input()