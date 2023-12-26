#TUPLAS (variáveis compostas)
#No MUNDO 3:
#   - estruturas compostas (variáveis compostas): TUPLAS, LISTAS E DICIONÁRIOS; 
#   - rotinas; tratamento de erros, etc.
lanche = ('Suco', 'Hambúrguer','Pizza', 'Pudim') #pode ser COM ou SEM parênteses
#As Tuplas são IMUTÁVEIS, ou seja, NÃO É POSSÍVEL MUDAR UM ELEMENTO DE DENTRO DELA.
#   Se eu quiser trocar o pudim, por ex, teria que parar o programa, mudar a tupla e depois continuar.
# print(lanche[0])
# print(lanche[-1]) #para mostrar o último elemento
# print(lanche[1:]) #espaço vazio: vai até o final
# print(lanche[:2])
# print(len(lanche)) #para saber o comprimento (nº de elementos)

#pos = posição
for pos, c in enumerate(lanche): #o enumerate mostra tanto o dado atribuído quanto sua posição
    print(f'Eu vou comer {c} na posição {pos}')


for cont in range(0, len(lanche)):
    #print(cont,end=' - ')
    print(f'Vou comer {lanche[cont]} na posição {cont}',end=' ') #quando precisar mostrar a posição

print(sorted(lanche)) #SORTED = ORGANIZADO (Fica em ordem alfabética)