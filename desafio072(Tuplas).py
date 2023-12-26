contagem = ('zero', 'um', 'dois', 'três', 'quatro',
'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
'onze', 'doze', 'treze', 'quatorze', 'quinze', 
'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    número = int(input('Digite um número: '))
    if 0 <= número <= 20:
            break
    print('Tente novamente! ',end='')
print(f'Você digitou o número {contagem[número]}')

#corrigido