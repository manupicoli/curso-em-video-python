#operações aritméticas
n1 = int(input('Insira um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma dos valores {}, \n a multiplicação é {} \n e a divisão é {}'.format(s, m, d), end=' ')
#o \n irá jogar o resto da frase para uma nova linha
#enquanto o end=' ' serve paara não dar quebra de linha entre um print e outro
print('A divisão inteira é {} e a exponenciação é {}'.format(di, e))

input()
