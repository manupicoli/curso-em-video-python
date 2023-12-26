n = int(input('Digite o termo inicial de uma PA: '))
r = int(input('Digite a razão da PA: '))
#os 10 primeiros termos de uma PA
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais #primeiro aparece o total (0) + os primeiros 10 termos
    while c <= total:
        print(f'{n}',end=' - ')
        n += r #o primeiro termo recebe n + razão a cada laço
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print(f'A sua progressão acabou com o total de {total} termos.')
