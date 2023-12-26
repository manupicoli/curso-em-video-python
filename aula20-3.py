#Retorno de valores = RETURN

def somar(a=0, b=0, c=0): 
    """
    Faz uma soma e mostra na tela.
    parametro a: primeiro valor
    parametro b: segundo valor
    parametro c: terceiro valor
    return: sem retorno
    """
    soma = a + b + c
    return soma

resp = somar(5, 6, 3)
resp1 = somar(8, 4)
print(f'Os resultados foram: {resp} e {resp1}')

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

print('-' * 50)

r1 = fatorial(5)
r2 = fatorial(6)
print(f'Os resultados foram: {r1} e {r2}')

print('-' * 50)

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
print(par(num))

if par(num):
    print('É par!')
else:
    print('Não é par!')