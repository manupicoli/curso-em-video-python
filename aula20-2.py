#FUNÇÕES PARTE 2

#Interactive Help
#função interna help()
# help()
#ou
# print(input.__doc__)

#DOCSTRINGS - basicamente uma string de documentação

def contador(inicio, fim, passo):
    """
    Faz uma contagem e mostra na tela.
    parametro inicio: inicio da contagem
    parametro fim: fim da contagem
    parametro passo: passo da contagem
    return: sem retorno
    """
    c = inicio
    while c <= fim:
        print(f'{c}', end=' ')
        c += passo
    print('FIM!')

help(contador)

#Parâmetros opcionais

def somar(a, b, c=0): # o c=0 significa que, se o c não receber nenhum número, ele vai ser igual a zero
    """
    Faz uma soma e mostra na tela.
    parametro a: primeiro valor
    parametro b: segundo valor
    parametro c: terceiro valor
    return: sem retorno
    """
    soma = a + b + c
    print(f'A soma dos números é igual a {soma}.')

somar(5, 6, 3)
somar(8, 4)

#Escopo de variáveis
# é o local onde uma variável vai existir e o local onde a variável não vai mais existir

def teste():
    x = 8 # a variável x só existe dentro da função teste, então se chamar ela fora da função, vai dar erro
    #VARIÁVEL LOCAL
    print(f'Na função teste, n vale {n}') #já o n pode ser chamado dentro da função, mesmo estando fora dela
    print(f'Na função teste, x vale {x}')

n = 2 #já o n pode ser chamado dentro da função, mesmo estando fora dela; VARIÁVEL GLOBAL
print(f'No programa principal, n vale {n}')
teste()

def funçao(b):
    global a # quando usamos o global, ele não cria a variável local, e substitui o valor do a global
    a = 7
    b += 4
    print(f'A vale {a}')
    print(f'B vale {b}')

a = 9
funçao(a)
print(f'A vale {a}')
