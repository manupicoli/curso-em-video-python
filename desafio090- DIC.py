aluno = dict()
aluno['Nome'] = input('Nome do aluno: ').title()
aluno['Média'] = float(input('Média do aluno: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'APROVADO'
else:
    aluno['Situação'] = 'REPROVADO'
    
for nome, valor in aluno.items():
    print(f'{nome} é igual a {valor}')

#corrigido