galera = list()
dado = list()
maior = 0
menor = 0

while True:
    dado.append(input('Nome: '))
    dado.append(int(input('Peso: ')))
    if len(galera) == 0:
        maior = dado[1]
        menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    galera.append(dado[:])
    dado.clear()
    continuar = input('Deseja continuar? [S/N]: ').title()
    if continuar in 'N':
        break

print(f'No total, {len(galera)} pessoas foram cadastradas.')
print(f'O maior peso foi de {maior}kg, peso de ',end='')

for pessoa in galera:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}]',end=' ')

print()
print(f'O menor peso foi de {menor}kg, peso de ',end='')

for pessoa in galera:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}]',end=' ')

#corrigido