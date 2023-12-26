dados = dict()
lista_gols = list()
total = 0
nome = input('Nome do jogador: ').title()
dados['Nome'] = nome

partidas = int(input(f'Quantas partidas {nome} jogou? '))
for partida in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {partida}? '))
    lista_gols.append(gols)
    total += gols

dados['Gols'] = lista_gols
dados['Total'] = total

print(f'O jogador {nome} jogou {partidas} jogos.')

for numero in range(0, partidas):
    print(f'Na partida {numero} ele fez {lista_gols[numero]} gols.')

print(f'Foi um total de {dados["Total"]} gols.')

#corrigido