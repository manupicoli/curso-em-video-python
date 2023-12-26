print('Bem-vindo(a) a nossa loja!')
total = 0
mais1000 = 0
maisbarato = 0
nomemaisbarato = ''
cont = 0

while True:
    nome = input('Digite o nome do seu produto: ').title()
    preço = int(input('Qual é o preço do seu produto? R$'))
    total += preço
    cont += 1
    if preço > 1000:
        mais1000 += 1
    if cont == 1 or preço < maisbarato:
        maisbarato = preço
        nomemaisbarato = nome
    c = input('Quer continuar? [S/N]: ').upper()
    while c != 'S' and c != 'N':
        c = input('Quer continuar? [S/N]: ').upper()
    if c == 'S':
        print('Certo!')
    if c == 'N':
        break
print(f'O total da compra foi de {total} reais')
print(f'{mais1000} produto(s) custam mais de R$1000')
print(f'O produto mais barato foi a(o) {nomemaisbarato}, que custa R${maisbarato:.2f}.')