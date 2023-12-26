#LISTAS PARTE 2
pessoas = list()
dados = ('Pedro', 19)
pessoas.append(dados[:]) #COLOCAR UMA LISTA DENTRO DA OUTRA
#print(pessoas)
#print(pessoas[0][0]) #dentro do item 0 de pessoas, quero o item 0 da lista dados
galera = [['Ana', 20], ['Maria', 87], ['Guilherme', 56], ['Pedro', 15]]
for pessoa in galera:
    print(pessoa) #se quiser só o nome: pessoa[0] ; só a idade pessoa[1]

pessoal = list()
dado = list()
for c in range(0, 3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    pessoal.append(dado[:]) #pessoal vai receber uma cópia de dado
    dado.clear() #assim, mesmo limpando os dados dps, ainda vai ser possível ver os dados dentro da lista pessoal

for pessoa in pessoal:
    if pessoa[1] > 21:
        print(f'{pessoa[0]} tem mais de 21 anos.')
