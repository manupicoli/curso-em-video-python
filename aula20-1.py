#FUNÇÕES PARTE 1

def mostra_linha(): #o def cria funções, comandos personalizados
    print('-' * 30)

mostra_linha()
print('Curso em vídeo')
mostra_linha()
print()

#também é possível criar parâmetros

def mensagem(msg): #o MSG é um parâmetro
    print('-' * 30)
    print(msg)
    print('-' * 30)

mensagem('Curso em vídeo') #define-se o parâmetro

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B vale {s}')

soma(10, 5)

#DESEMPACOTAR PARÂMETROS

def contador(*num): # o * significa que voce nao sabe quantos parametros num vai receber, mas a função
#sempre vai mostrar todos eles
#ele automaticamente cria um TUPLA; a desvantagem é que a tupla é imutável
    tam = len(num)
    print(f'Ao todo, recebi {tam} números')

contador(5, 6, 2, 3)

def contador(*num):
    for valor in num:
        print(valor, end='')
    print('FIM!')

#também é possível utilizar listas
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [1, 4, 5, 2, 3, 9]
dobra(valores)
print(valores)
