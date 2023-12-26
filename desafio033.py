n = float(input('Primeiro valor: '))
m = float(input('Segundo valor: '))
b = float(input('Terceiro valor: '))
#Verificando o menor valor
menor = n
if m<b and m<n:
    menor = m
if b<m and b<n:
    menor = b
#Verificando o maior valor
maior = n
if m>n and m>b:
    maior = m
if b>n and b>m:
    maior = b
print('O menor valor é {} e o maior valor é {}'.format(menor, maior))
