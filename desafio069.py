print('Seja bem-vindo(a)! Vamos fazer seu cadastro: ')
mais18 = 0
homens = 0
Mmenos20 = 0
while True:
    n = input('Digite seu nome: ').upper()
    i = int(input('Digite sua idade: '))
    s = input('Digite seu sexo: [F/M] ').upper()
    while s != 'F' and s != 'M':
        s = input('Digite seu sexo: [F/M] ').upper()
    c = input('Gostaria de fazer mais cadastros? [S/N]: ').upper()
    while c != 'S' and c != 'N':
        c = input('Gostaria de fazer mais cadastros? [S/N]: ').upper()
    if c == 'S':
        print('Certo! Vamos continuar.')
    if i > 18:
        mais18 += 1
    if s == 'M':
        homens += 1
    if s == 'F' and i < 20:
        Mmenos20 += 1
    if c == 'N':
        print('Encerrando.')
        break
print(f'Ao todo, {mais18} pessoas tem mais de 18 anos;')
print(f'Foram cadastrados {homens} homens;')
print(f'Foram cadastradas {Mmenos20} mulheres com menos de 20 anos.')
