matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
terceira_coluna = []
maior = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição {linha, coluna}: '))
        if matriz[linha][coluna] % 2 == 0:
            pares.append(matriz[linha][coluna])
        if coluna == 2:
            terceira_coluna.append(matriz[linha][coluna])
        if linha == 1 and matriz[linha][coluna] > maior:
            maior = matriz[linha][coluna]

print('--' * 30)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^6}]',end='')
    print()

print('--' * 30)
print(f'A soma de todos os valores pares digitados foi {sum(pares)}') #tb é possivel faer isso com somadores s += matriz[linha][coluna]
print(f'A soma de todos os valores da terceira coluna foi {sum(terceira_coluna)}')  
print(f'O maior valor da segunda linha foi {maior}')

#corrigido