continuar = 'S'
lista = []
idades = 0
mulheres = []
acima_idade = []

while continuar == 'S':
    pessoa = dict()
    pessoa['Nome'] = input('Nome: ').title()
    pessoa['Sexo'] = input('Sexo [M/F]: ').upper()

    while pessoa['Sexo'] not in 'MF':
        pessoa['Sexo'] = input('Sexo [M/F]: ').upper()

    pessoa['Idade'] = int(input('Idade: '))
    lista.append(pessoa)

    idades += pessoa['Idade']
    media = idades / len(lista)

    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa['Nome'])
    
    if pessoa['Idade'] > media:
        acima_idade.append(pessoa)

    continuar = input('Quer continuar? [S/N]: ').upper()
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]: ').upper()

print(lista)
print(f'O grupo tem {len(lista)} pessoas')
print(f'A média de idade do grupo é {media:.2f}')
print(f'As mulheres cadastradas foram: {mulheres} ')
print(f'Lista de pessoas que estão acima da idade média: {acima_idade}')

#corrigido