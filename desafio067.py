while True:
    n = int(input('Digite um número para saber a sua tabuada: '))
    if n > 0:
        for c in range(1, 11):
            t = n * c
            print(f'{n} x {c} = {t}')
    if n < 0:
        break
print('Programa TABUADA encerrado.')

#corrigido