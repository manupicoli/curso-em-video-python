média = mav = mev = c =  0
r = 'S'
while r == 'S' :
    num = int(input('Digite um valor inteiro: '))
    r = input('Deseja digitar mais valores? [S/N]: ').upper()
    c += 1 
    média += num
    if c == 1:
        mav = mev = num
    else:
        if num > mav:
            mav = num
        if num < mev:
            mev = num
    if r == 'N':
        print('Certo!')

print(f'A média dos valores digitados é {(média) / c:.2f}')
print(f'O maior valor foi {mav} e o menor valor foi {mev}.')
