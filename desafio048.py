s = 0 #acumulador, igual a zero pq ainda não recebe nenhum valor
cont = 0 #contador, pq até agora não conta nenhum número
for c in range(0, 501, 3):
    if c % 2 != 0:
        cont = cont + 1 #cada vez que achar um número divisível por três, recebe cont + 1
        s += c #aqui ACUMULA o que já tem com o número obtido pelo laço c
print(f'A soma de todos {cont} os valores é {s}')