n = int(input('Digite um valor de 0 a 9999: '))
u = n // 1 % 10
#essa é a forma mais fácil matematicamente falando, mas também é possível resolver esse problema usando If
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('A unidade é igual a {}, a dezena é igual a {},'.format(u, d), end=' ')
print('a centena é {} e o milhar é {}'.format(c, m))
