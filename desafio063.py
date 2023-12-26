n = int(input('Quantos termos da sequência de Fibonacci você quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} - {t2}',end='')
c = 3 #começa no três pq ja tem os dois primeiros termos
while c <= n:
    t3 = t1 + t2
    print(f' - {t3}',end='')
    t1 = t2 #para fazer a PROGRESSÃO DE TERMOS
    t2 = t3
    c += 1
print(' - FIM')
