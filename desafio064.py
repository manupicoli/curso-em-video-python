n = int(input('Digite um número inteiro de até 3 dígitos (999 para parar): '))
s = 0
t = 0
while n != 999:
    n = int(input('Por favor, digite novamente: '))
    s += 1
    t += n
if n == 999:
    print(f'Certo! Você precisou de {s + 1} tentativas para chegar na condição de parada (999)!')
    print(f'A soma dos números digitados é {t - 999}!')
print('FIM')