from datetime import date
data2 = int(date.today().strftime('%Y'))   
ma = 0
me = 0
for c in range(1, 8):
    n = int(input(f'Digite o {c}º ano de nascimento: '))
    a = data2 - n
    if a >= 21:
        ma += 1
    else:
        me += 1

print(f'Tivemos {ma} pessoa(s) maiores de idade e {me} pessoa(s) menores de idade!')