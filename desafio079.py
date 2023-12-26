valores = []
while True:
    numero = int(input('Digite um número para adicioná-lo na lista: '))
    if numero in valores:
            print('Você já adicionou esse número! Escolha outro.')
    if numero not in valores:
        valores.append(numero)
        print('Número adicionado com sucesso.')
    cont = input('Deseja continuar? [S/N] ').upper()
    if cont == 'S':
        print('Certo!', end=' ')
    if cont == 'N':
        print('A lista gerada foi: ',end='')
        break
    while cont != 'S' and cont != 'N':
        cont = input('Deseja continuar? [S/N] ').upper()

valores.sort()
print(valores)

#certo