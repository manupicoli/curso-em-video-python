def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} marcou {gols} gols no campeonato.'



nome = input('Digite o nome do jogador: ').title()
gols_marcados = input('Quantidade de gols marcados: ')

if gols_marcados.isnumeric():
    gols_marcados = int(gols_marcados)
else:
    gols_marcados = 0

if nome.strip() == '':
    print(ficha(gols=gols_marcados))
else:
    print(ficha(nome, gols_marcados))

#corrigido