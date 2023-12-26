from datetime import date
n = int(input('Insira seu ano de nascimento: '))
data = date.today()
data2 = int(data.strftime('%Y'))
i = data2 - n
if i <= 9:
    print('Sua categoria é MIRIM!')
elif 9 < i <= 14:
    print('Sua categoria é INFANTIL!')
elif 14 < i <= 19:
    print('Sua categoria é JÚNIOR!')
elif i == 20:
    print('Sua categoria é SÊNIOR!')
else:
    print('Sua categoria é MASTER!')