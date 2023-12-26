lista = []
listapar = []
listaimpar = []
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    if numero % 2 == 0:
        listapar.append(numero)
    else:
        listaimpar.append(numero)
    cont = input('Deseja continuar? [S/N]: ').upper()
    while cont != 'S' and cont != 'N':
        cont = input('Deseja continuar? [S/N]: ').upper()
    # if cont == 'S':
    #     print('Certo!',end=' ') 
    # else:
    #     break ----------- ocupa menos linhas se fizer assim:
    if cont in 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista com números pares é {listapar}')
print(f'A lista com números impares é {listaimpar}')

#corrigido

