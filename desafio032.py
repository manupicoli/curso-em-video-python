n = int(input('Insira um ano qualquer: '))
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(n))
else:
    print('O ano {} NÃO é BISSEXTO!'.format(n))