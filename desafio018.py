import math
n = float(input('Digite o valor de um ângulo: '))
seno = math.sin(math.radians(n))
cosseno = math.cos(math.radians(n))
tangente = math.tan(math.radians(n))
print('O ângulo {} tem o seno {:.2f}, o cosseno {:.2f} e a tangente {:.2f}'.format(n, seno, cosseno, tangente))

input()
