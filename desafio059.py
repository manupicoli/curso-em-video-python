n = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
e = 0
while e != 5:
    print('''Selecione uma das opções do menu!
[1] Para SOMAR os valores\n[2] Para MULTIPLICAR os valores
[3] Para saber o MAIOR valor\n[4] Para escolher OUTROS VALORES
[5] Para SAIR do programa.''')
    e = int(input('Sua escolha: '))
    if e == 1:
        s = n + n2
        print(f'A soma dos dois valores é igual a {s}.')
    elif e == 2:
        m = n * n2
        print(f'A multiplicação dos dois valores é igual a {m}.')
    elif e == 3:
        if n > n2:
            print(f'O maior valor é {n}.')
        else:
            print(f'O maior valor é {n2}.')
    elif e == 4:
        n = int(input('Digite novamente um primeiro valor: '))
        n2 = int(input('Digite novamente um segundo valor: '))
    elif e == 5:
        print('Certo! Saindo do programa.')
print('Fim')