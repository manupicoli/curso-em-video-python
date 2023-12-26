import math
nome = input('Bom dia, seja bem vindo(a)! Qual é seu nome? ').title()
valor = int(input(f'Qual o valor da casa que você deseja comprar, {nome}? '))
salário = int(input('Qual o valor do seu salário? '))
anos = int(input('Durante quantos anos você deseja pagar por esta compra? '))

m = valor / (anos * 12)
num = math.ceil(m)

if m < 0.3 * salário:
    print(f'Parabéns! O seu empréstimo será aprovado e você deverá pagar {num} reais mensais durante {anos} anos.')
else:
    print('Valor de empréstimo negado! Gostaria de procurar por outros itens?')

input()