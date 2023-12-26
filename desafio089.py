continuar = 'S'
dados = []

while continuar == 'S':
    nome = input('Nome: ').title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    # dados.append(nome)
    # dados.append(nota1)
    # dados.append(nota2)
    # dados.append(media)
    continuar = input('Deseja contiuar? [S/N] ').title()

print(f'{"Nº":>4}{"Nome":>10}{"Média":>10}')
for indice, pessoa in enumerate(dados):
    print(f'{indice:>4}{pessoa[0]:>10}{pessoa[2]:>10}')

while True:
    aluno = int(input('A nota de qual aluno você deseja conferir? (999 interrompe) '))
    if aluno == 999:
        break
    if aluno <= len(dados) - 1:
        print(f'As notas de {dados[aluno][0]} são {dados[aluno][1]}')

print('Volte sempre!')

#corrigido