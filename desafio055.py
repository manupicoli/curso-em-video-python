maior = 0 
menor = 0
for c in range(1, 6):
    n = float(input(f'Insira o peso da {c}ª pessoa: '))
    if c == 1: 
        maior = n #se não tem nenhum outro valor, o maior e o menor vai ser ele mesmo (n)
        menor = n
    else:
        if n > maior: #se houver algum maior, a variavel vai receber esse valor
            maior = n
        if n < menor:
            menor = n

print(f'O maior peso lido foi {maior}kg e o menor foi {menor}kg')