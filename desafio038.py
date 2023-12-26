n = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n > n2:
    print(f'O número {n} é maior que {n2}')
elif n < n2:
    print(f'O número {n} é menor que {n2}')
elif n == n2:
    print(f'Os números são iguais!')