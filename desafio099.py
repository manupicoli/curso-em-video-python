def ver_maior(*num):

    print(f'Analisando os valores passados...')
    print(f'{num} foram informados {len(num)} valores ao todo.')

    maior = 0

    for valor in num:
        if valor > maior:
            maior = valor

    print(f'O maior valor informado foi {maior}')
    print('-' * 40)

ver_maior(10, 6, 4, 17, 4, 2)
ver_maior(90, 76, 54, 120, 45, 290)
ver_maior(0)

#corrigido