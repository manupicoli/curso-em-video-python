n = int(input('Digite o valor do seu salário para saber qual será seu aumento: '))
if n>1250:
    a = (n / 100) * 10 
    t = a + n
    print('O valor do seu aumento será de {}, totalizando um salário de {}'.format(a, t))
else:
    a2 = (n / 100) * 15
    t2 = a2 + n
    print('O valor do seu aumento será de {}, totalizando um salário de {}'.format(a2, t2))
    