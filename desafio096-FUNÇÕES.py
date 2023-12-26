def area(largura, comprimento):
    area_total = largura * comprimento
    print(f'A área total do terreno {largura}x{comprimento} é {area_total}m2')


l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)

#corrigido