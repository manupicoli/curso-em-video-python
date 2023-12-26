valores = []
for c in range(0, 5):
    numero = int(input('Digite um número: '))
    if c == 0 or numero > valores[-1]: #se o c == 0, então é o primero número e o valores[-1] significa o último da lista
        valores.append(numero)
        print('Adicionado ao final da lista...')
    else:
        pos = 0 
        while pos < len(valores): #vai verificar da posição 0 até o último item da lista
            if numero <= valores[pos]: #vai ver se tem um número menor ou igual a ele
                valores.insert(pos, numero) #se tiver, vai inserir naquela posição
                print(f'Adicionado na posição {pos}...')
                break
            pos += 1

print(valores)

#corrigido