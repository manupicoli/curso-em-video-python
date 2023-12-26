numeros = [[], []]

for numero in range(1, 8):
    valor = int(input(f'Informe o {numero}º número: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

numeros[0].sort()
numeros[1].sort()
print(f'Os valores ímpares digitados foram {numeros[1]}')
print(f'Os valores pares digitados foram {numeros[0]}')

#corrigido