p = float(input('Qual é o preço do produto? '))

print('Qual a condição de pagamento? \n Digite 1 para À VISTA NO DINHEIRO; \n Digite 2 para À VISTA NO CARTÃO;', end=' ')
print('\n Digite 3 para ATÉ 2X NO CARTÃO; \n Digite 4 para 3X OU MAIS NO  CARTÃO')

c = float(input('Digite: '))


if c == 1:
    t = p - (0.10 * p)
    print(f'Você pagará {t} reais no produto final.')
elif c == 2:
    t2 = p - (0.05 * p)
    print(f'Você pagará {t2} reais no produto final.')
elif c == 3:
    print(f'Você pagará {p} reais no produto final.')
else:
    t3 = p + (0.2 * p)
    print(f'Você pagará {t3} reais no produto final.')

input()