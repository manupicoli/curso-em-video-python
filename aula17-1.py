#LISTAS - Elas PODEM ser mutáveis
lista = ['hamburguer', 'pudim', 'suco', 'bolo']
lista[2] = 'brownie'
lista.append('cookie') #para adicionar um item no final da lista
print(lista)
lista.insert(0, 'salsicha') #para adicionar um item em uma posição específica
print(lista)
del lista[3] #para deletar algum item
print(lista)
lista.pop(1) #geralmente, POP é usado para deletar o ÚLTIMO elemente, mas tb pode ser usado com o índice
print(lista)
lista.remove('bolo') #tem que escrever o item que você quer remover
print(lista)
if 'bolo' in lista: #quando não se tem certeza se um item está ou não na lista
    lista.remove('bolo')