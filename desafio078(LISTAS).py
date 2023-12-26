mai = 0
men = 0
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = valores[c]
        men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < men:
            men = valores[c]


print(f'A lista gerada foi {valores}')
print(f'O maior valor digitado foi {mai} na(s) posição(ões) ',end='')
for pos, v in enumerate(valores):
    if v == mai:
        print(f'{pos}...',end=' ')
print(f'\nO menor valor digitado foi {men} na(s) posição(ões) ',end='')
for pos, v in enumerate(valores):
    if v == men:
        print(f'{pos}...',end=' ')

#corrigido
