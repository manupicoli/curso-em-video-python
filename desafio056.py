idade = 0 #int
maioridadehomem = 0 #int
nomemaisvelho = '' #str
mu = 0 #int
for c in range(1, 5):
    print(f'{c}ª PESSOA:')
    n = input('Nome: ').title()
    i = int(input('Idade: '))
    s = input('Sexo (F/M): ').title()
    idade += i
    if c == 1 and s == 'M':
        maioridadehomem = i
        nomemaisvelho = n
    if s == 'M' and i > maioridadehomem:
        maioridadehomem = i
        nomemaisvelho = n
    if i < 20 and s == 'F':
        mu += 1

print(f'A média de idades é {idade / 4}')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomemaisvelho}.')
print(f'Ao todo, há {mu} mulher(es) com menos de 20 anos.')