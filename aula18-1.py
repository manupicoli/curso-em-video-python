#DICIONÁRIOS
#NAS LISTAS, CADA ELEMENTO É RECONHECIDO POR UM INDICE NUMÉRICO
#Já nos dicionários, é possível que os indices sejam palavras, indices literais, personalizados
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
#Para adicionar um novo elemento, não é necessário usar APPEND:
dados['sexo'] = 'M'
print(dados)
#Para remover um elemento:
del dados['idade']
print(dados)

#os inidices, no python, são chamados de CHAVES ou KEYS
filmes = {'título': 'Shrek',
        'ano': 2001,
        'diretor': 'Vicky Jenson e Andrew Adamson'
}
print(filmes)
#para mostrar apenas os valores, ou seja, o VALOR que cada CHAVE recebeu
print(filmes.values())
#para mostrar as chaves:
print(filmes.keys())
#para mostrar os dois:
print(filmes.items())
#parecido com o enumerate nas listas:
for chave, valor in filmes.items(): 
        print(f'O {chave} é {valor}')

print(filmes.items)
