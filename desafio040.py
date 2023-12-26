n = float(input('Insira sua primeira nota: '))
n2 = float(input('Insira sua segunda nota: '))
m = (n + n2) / 2
if m < 5:
    print('Você foi REPROVADO!')
elif 5 <= m <= 6.9:
    print('Você pegou RECUPERAÇÃO!')
elif m >= 7:
    print('Você está APROVADO!')
