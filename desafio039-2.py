from datetime import date
nome = int(input('Qual é o ano do seu nascimento? '))
data = date.today()
data2 = int(data.strftime('%Y'))
#data = date.today().year
idade = (int(data2 - nome))
print(f'Você completa {idade} anos em {data2}')
if idade < 18:
    saldo = 18 - idade
    print(f'Portanto, ainda precisará se alistar para o serviço militar em {saldo} ano(s). Fique atento!')
elif idade > 18:
    saldo2 = idade - 18
    print(f'Portanto, já cumpriu com o alistamento há {saldo2} ano(s).')
elif idade == 18:
    print('Portanto, chegou a hora de se alistar no serviço militar! Consulte as datas e se informe.')