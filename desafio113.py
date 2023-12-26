def leiaInt(msg):
    while True:
        try:
            n = int(input(msg)) 
        except (ValueError, TypeError):
            print('ERRO! Por favor, digite um número válido')
            continue
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número')
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg)) 
        except (ValueError, TypeError):
            print('ERRO! Por favor, digite um número válido')
            continue
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número')
        else:
            return n

n = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {n} e o número real {n2}')