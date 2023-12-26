#Laços de repetição - parte 2 (estrutura de repetição com teste logico)
#Para usar o FOR, é necessário saber onde COMEÇA e onde TERMINA.
#Para usar o WHILE, não precisamos saber onde começa e termina, mas sim de uma CONDIÇÃO:
#ex: ENQUANTO não chegar na maçã, dê passos.

#for c in range(1, 10):
#   print(c)

c = 1 #contador igual a 1
while c < 10:
    print(c, end=' ')
    c += 1 #quando repetir, ele vai somando mais um a cada nova repetição

#só vai parar quando digitar o valor 0 (CONDIÇÃO DE PARADA)
n = 1
while n != 0:
    n = int(input('Digite um número: '))
print('FIM')

r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')