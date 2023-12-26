from random import randint
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
mega_sena = []
lista_random = []
total = 1
while total <= jogos:
    cont = 0
    while cont < 6:
        num = randint(1, 61)
        if num not in mega_sena:
            mega_sena.append(num)
            cont += 1
    mega_sena.sort()
    lista_random.append(mega_sena[:])
    mega_sena.clear()
    total += 1

#o indice vai pegar a posição lista_random[0], lista_random[1], etc. e a lista vai pegar o conteúdo
for indice, lista in enumerate(lista_random):
    print(f'Jogo {indice + 1}: {lista}')
#corrigido