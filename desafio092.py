from datetime import date
dados = dict()
dados['Nome'] = input('Nome: ').title()
ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today()
idade = ano_atual.year - ano_nascimento
dados['Idade'] = idade
dados['CTPS'] = int(input('Nº da Carteira de Trabalho (Digite 0 se não tiver): '))

if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = int(input('Salário: R$'))
    ano_aposentadoria = dados['Contratação'] + 35
    aposentado = ano_aposentadoria - ano_nascimento
    dados['Aposentadoria'] = aposentado

for valor, chave in dados.items():
    print(f'{valor} tem o valor {chave}')
#certo