nome = input('Qual é o seu nome? ').title().strip()
if (nome == 'Manuela'):
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))
n1 = float(input('Digite sua primeira nota, por favor: '))
n2 = float(input('Agora a segunda nota, por favor: '))
m = (n1 + n2)/2
print('A média das suas notas foi {:.1f}'.format(m))
if m<=6.9:
    print('Sua média é insuficiente!')
else:
    print('Parabéns! Você está acima da média')
