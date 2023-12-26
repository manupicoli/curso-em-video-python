import random
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolhido = random.choice(n)
num = int(input('Tente adivinhar o número escolhido...: '))
p = 0
while num != escolhido:
    num = int(input('Você errou! Tente novamente: '))
    p += 1
    if num < escolhido:
        print('Mais... Tente novamente.')
    elif num > escolhido:
        print('Menos... Tente novamente.')
    if num == escolhido:
        print(f'Parabéns! Você acertou. O computador escolheu {escolhido} e você escolheu {num} em {p + 1} tentativas!')
