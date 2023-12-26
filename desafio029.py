n = int(input('Qual foi a velocidade do seu carro? '))
m = (n - 80) * 7
if n<=80:
    print('Você não foi multado')
else:
    print('Você foi multado! O valor da sua multa foi de {} reais'.format(m))