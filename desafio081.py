valores = []
e = 1
while True:
    valores.append(int(input('Digite um número: ')))
    continuar = input('Deseja continuar? [S/N] ').upper()
    while continuar != 'S' and continuar != 'N':
        continuar = input('Deseja continuar? [S/N]: ').upper()
    if continuar == 'S':
        e += 1
    if continuar == 'N':
        break

if 5 in valores:
    print(f'O número cinco está na lista, na posição {valores.index(5)}.')
else:
    print('O número cinco não está na lista!')
valores.sort(reverse=True)
print(f'Você digitou {e} elementos.') #tb poderia usar a função len(valores) para descobrir o nº de elementos
print(f'A lista em ordem decrescente fica {valores}')

#certo