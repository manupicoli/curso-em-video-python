n = int(input('Digite um valor: '))
is_primo = True
for c in range(1, n+1):
    if n % c == 0 and c != 1:
        if c != n:
            is_primo = False

print(is_primo)
