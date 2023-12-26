def fatorial(numero, show=False):
    """
    Calcula o fatorial de um número.
    -> numero: é o numero a ser calculado.
    -> show: (opcional) mostrar ou não a conta.
    -> return: o valor fatorial de um numero n.
    """
    f = 1
    if show == False:
        for c in range(numero, 0, -1):
            f *= c
        return f
    else:
        for c in range(numero, 0, -1):
            f *= c
            if c != 1:
                print(f'{c} x ',end='')
            else:
                print(f'{c} = ',end='')
        return f


print(fatorial(5))

num = int(input('Digite um número para saber seu fatorial: '))
print(fatorial(num, False))

#corrigido