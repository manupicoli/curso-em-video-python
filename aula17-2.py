import random
valores = list(range(4, 11)) #para criar uma lista automaticamente
números = [3, 9, 6, 1, 5, 10]
números.sort()
print(números)
números.sort(reverse=True)
print(números)
print(len(números))

for pos, v in enumerate(números): #para achar a posição e o seu respectivo valor
    print(f'Na {pos + 1 }ª posição, encontrei o valor {v}!')

#para criar uma lista a partir de valores digitados no teclado
valores = list()
for cont in range(1, 6):
    valores.append(int(input('Digite um número: ')))
print(valores)

a = [1, 3, 5, 7]
b = a #quando eu igualo 2 listas, cria-se uma ligação entre elas: se alterar o elemento de uma, alterará na outra tb
print(f'A lista A {a} é igual a lista B {b}')

#Para criar uma CÓPIA:
b = a[:] #b vai receber todos os itens de a ([:} SIGNIFICA UM FATIAMENTO COMPLETO])
b[2] = 8
print(f'Lista A {a} e lista B {b}')