import math
n = int(input('Digite o valor do cateto oposto: '))
n2 = int(input('Digite o valor do cateto adjacente: '))

h = math.sqrt(n**2 + n2**2)

print('A hipotenusa desse triãngulo equivale a {:.2f}'.format(h))

input()