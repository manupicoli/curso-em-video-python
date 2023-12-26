n = int(input('Digite um valor: '))
#para ser primo precisa ser divisel apenas por 1 e ele mesmo
primo = 0
for c in range(1, n +1):
    if n % c == 0:
        primo += 1

if primo <= 2:
    print(f'O número {n} foi divisível {primo} vezes. Portanto, ele é primo!')
else:
    print(f'O número {n} foi divisível {primo} vezes. Portanto, ele não é primo!')
