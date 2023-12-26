a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(sorted(c))
#propriedades da TUPLA
print(c.count(5))
print(c.index(8)) #em qual posição está o 8
print(c.index(5, 2))#index sempre mostra a primeira ocorrência (p) de um número (n). 
#Para ignorar a primeira ocorrência (p): (n, p + 1) = DESLOCAMENTO.

#No Python, é possível colocar strings e números em uma mesma Tupla.
pessoa = ('Gustavo', 39, 'M', 99.8)
print(pessoa)
del(pessoa) #del = delete (vai APAGAR A TUPLA ou qualquer outra variável dentro do Python)