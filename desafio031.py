n = int(input('Qual a distância, em km, do local de origem até seu destino? '))
if n<=200:
    m = n * 0.50
    print('O valor da sua passagem será {} reais.'.format(m))
else:
    v = n * 0.45
    print('O valor da sua passagem será {:.2f} reais.'.format(v))

