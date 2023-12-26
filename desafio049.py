n = int(input('Digite um número para ver sua tabuada: '))
print(f'A tabuada de {n} é:', end=(' '))
for c in range(0, 11):
    a = n * c 
    print(a, end=('  '))
