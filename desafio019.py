import random
n = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n, n2, n3, n4]

escolhido = random.choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))