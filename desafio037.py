n = int(input('Escolha um número: '))
print('Escolha qual será a base de conversão: \n Digite 1 para BINÁRIO', end=' ')
print('\n Digite 2 para OCTAL \n Digite 3 para HEXADECIMAL')
#ou print('''Escolha qual será a base de conversão:
#Digite 1 para BINÁRIO'
#Digite 2 para OCTAL 
#Digite 3 para HEXADECIMAL''')
e = int(input('Sua escolha: '))

if e == 1:
    print(f'O número {n} convertido para BINÁRIO é igual a {bin(n) [2:]}')
elif e == 2:
    print(f'O número {n} convertido para OCTAL é igual a {oct(n) [2:]}')
elif e == 3:
    print(f'O número {n} convertido para HEXADECIMAL é igual a {hex(n) [2:]}')
else:
    print('Opção inválida. Tente novamnte.')