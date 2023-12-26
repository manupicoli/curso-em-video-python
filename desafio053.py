n = input('Digite uma frase: ').strip().upper()
f = n.split()
j = ''.join(f)
inverso = ''
for c in range(len(j) - 1, -1, -1): #vai da ultima letra até a primeira, voltando uma letra (contagem regressiva)
    inverso += j[c]
print(j, inverso)
if j == inverso:
    print('Temos um palíndromo!')
else:
    print('Não é palíndromo!')