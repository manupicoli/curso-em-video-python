#Estruturas de controle
#Condições aninhadas
# - colocar uma coisa dentro da outra (estruturas condicionais dentro de estruturas condicionais)
# if carro.esquerda():
# else if carro.direita():
# elif (abreviação) carro.ré():
# else:
# pode ter vários elifs dentro de um if, mas apenas 1 ou nenhum else.

nome = input('Qual é o seu nome? ').title()
if nome == 'Manuela':
    print('Que nome lindo!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é popular no Brasil!')
elif nome in 'Ana Jéssica Carolina Letícia':
    print('Belo nome feminino')
else: 
    print('Seu nome é normal!')
print(f'Tenha um bom dia, {nome}!')