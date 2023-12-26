def leiaInt(msg):
    valor = 0
    ok = False
    while True:
        n = input(msg)    
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'Erro! Digite um número válido.')
        if ok == True:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

#corrigido