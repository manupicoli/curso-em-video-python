n = int(input('Digite o termo inicial de uma PA: '))
r = int(input('Digite a razão da PA: '))
#os 10 primeiros termos de uma PA
c = 1
while c <= 10:
    print(f'{n}',end=' - ')
    n += r #o primeiro termo recebe n + razão a cada laço
    c += 1
print('FIM')