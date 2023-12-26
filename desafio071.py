while True:
    n = int(input('Qual o valor que você deseja sacar? R$'))
    resultado = n // 50
    print(f'Você vai precisar de {resultado} cédulas de 50 reais.')
    resto = n - (resultado * 50)
    if resto != 0:
        if resto >= 20:
            resultado2 = resto // 20
            print(f'Você vai precisar de {resultado2} cédulas de 20 reais.')
            resto2 = resto - (resultado2 * 20)
            if resto2 >= 10:
                resultado3 = resto2 // 10
                print(f'Você vai precisar de {resultado3} cédulas de 10 reais.')
                resto3 = resto2 - (resultado3 * 10)
                if resto3 >= 1:
                    resultado4 = resto3 // 1
                    print(f'Você vai precisar de {resultado4} cédulas de 1 real.')
            if resto2 < 10:
                resultado5 = resto2 // 1
                print(f'Você vai precisar de {resultado5} cédulas de 1 real.')
        if resto < 20:
            resultado6 = resto // 10
            print(f'Você vai precisar de {resultado6} cédulas de 10 reais.')
            resto4 = resto - (resultado6 * 10)
            if resto4 < 10:
                resultado7 = resto4 // 1
                print(f'Você vai precisar de {resultado7} cédulas de 1 real.')
    c = input('Deseja continuar? [S/N]: ').upper()
    if c == 'S':
        print('Certo!')
    if c == 'N':
        break
print('Muito obrigado!')
