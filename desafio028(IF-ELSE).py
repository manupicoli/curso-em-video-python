import randoms
n = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(n)
num = int(input('Tente a sorte... Escolha um número inteiro de 0 a 5...: '))
if escolhido ==  num:
    print('As forças místicas estão do seu lado hoje... ACERTOU!')
else:
    print('Não foi dessa vez! ERROU')
