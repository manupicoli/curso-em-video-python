n = int(input('Digite o termo inicial de uma PA: '))
r = int(input('Digite a razão da PA: '))

for c in range(n, (r * 10) + n, r):
    print(c, end=' ')
