palavras = ('gato', 'amor', 'aprender', 'programar', 'caneta', 'livro', 'mercado')
for p in palavras:
    print(f'\nNa palavra {p.upper()} as vogais são:',end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')


#corrigido