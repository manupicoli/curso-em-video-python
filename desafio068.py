import random
print('Vamos jogar PAR ou ÍMPAR!')
lista = [0, 1, 2, 3 , 4, 5, 6, 7, 8, 9, 10]
cont = 0
while True:
    n = int(input('Digite um número: '))
    e = input('Você quer PAR ou ÍMPAR? [P/I]: ').upper()
    c = random.choice(lista)
    soma = n + c
    if soma % 2 == 0:
        if e == 'P':
            print(f'Você GANHOU! O computador jogou {c} e você jogou {n}.')
            cont += 1
        if e == 'I':
            print(f'Você PERDEU! O computador jogou {c} e você jogou {n}.')
            break
    if soma % 2 != 0:
        if e == 'I':
            print(f'Você GANHOU! O computador jogou {c} e você jogou {n}.')
            cont += 1
        else:
            print(f'Você PERDEU! O computador jogou {c} e você jogou {n}.')
            break

print(f'O jogo foi finalizado após {cont} vitória(s) consecutivas.')


