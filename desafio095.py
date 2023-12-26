lista_gols = list()
jogadores = list()
dados = dict()
total = 0

continuar = 'S'
while continuar == 'S':
    lista_gols.clear()
    dados.clear()  
    nome = input('Nome do jogador: ').title()
    dados['Nome'] = nome
    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    for partida in range(0, partidas):
        gols = int(input(f'Quantos gols na partida {partida}? '))
        lista_gols.append(gols)
        total += gols
    dados['Gols'] = lista_gols[:]
    dados['Total'] = total
    total = 0
    jogadores.append(dados.copy())

    continuar = input('Quer continuar? [S/N]: ').upper()
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]: ').upper()

print('cod ', end='')
for elemento in dados.keys():
    print(f'{elemento:<20}', end='')
print()
print('-' * 60)
for indice, jogador in enumerate(jogadores):
    print(f'{indice:>3} ', end='')
    for dados in jogador.values():
        print(f'{str(dados):<20}', end='')
    print()
print('-' * 60)

while True:
    dados_jogador = int(input('Mostrar dados de qual jogador? '))

    if dados_jogador in range(0, len(jogadores)):
        print(f'O jogador {jogadores[dados_jogador]["Nome"]} jogou {len(jogadores[dados_jogador]["Gols"])} jogos.')
        for numero in range(0, len(jogadores[dados_jogador]["Gols"])):
            print(f'Na partida {numero} ele fez {jogadores[dados_jogador]["Gols"][numero]} gols.')
    if dados_jogador == 999:
        break
    else:
        print(f'Erro! Não existe jogador com código {dados_jogador}')

#corrigido