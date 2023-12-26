#também é possível misturar listas, tuplas e dicionários
locadora = [{'título': 'Shrek',
        'ano': 2001,
        'diretor': 'Vicky Jenson e Andrew Adamson'}, 
        {'título': 'Carros',
        'ano': 2006,
        'diretor': 'John Lasseter'},
        {'título': 'Show de Truman',
        'ano': 1998,
        'diretor': 'Peter Weir'}]

print(locadora[0]['ano'])

estado = dict()
brasil = list()

for contador in range(0, 3):
    estado['uf'] = input('Digite uma Unidade Federativa: ').title()
    estado['sigla'] = input('Digite a sigla desse estado: ').upper()
    brasil.append(estado.copy()) #ao invés de usar [:] para fazer a cópia, pode-se usar essa função própria de dict

for est in brasil:
    for nome, sigla in est.items(): #sempre a chave e o valor que ela recebe
        print(f'O campo {nome} recebeu o valor {sigla}')

