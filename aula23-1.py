# TRY 
# EXCEPT
try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    r = a / b
except Exception as erro: #usar o exception para mostrar o tipo de erro encontrado
#pode haver mais de um except, cada um mostrando um tipo de erro diferente
    print(f'O problema encontrado foi {erro.__class__} ')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero')
else: #com o else, nao aparece o erro na tela -> tratamento de erro -> é opcional
    print(f'O resultado é {r}')
finally: #vai executar independentemente de dar erro; tb é opcional
    print('Volte sempre!') 