listagem = ('Pão', 1, 
'Leite', 3.79, 
'Sucrilhos', 8.90, 
'Farinha', 3, 
'Manteiga', 10.90)
print('-' * 30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-' * 30)

for pos in range(len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='') # .< = postos alinhados à esquerda
    else:
        print(f'R${listagem[pos]:>7.2f}')

#corrigido
