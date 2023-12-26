valores = []
for v in range(0, 5):
    numero = int(input('Digite um valor para adicioná-lo na lista: '))
    if len(valores) == 0:
        valores.insert(0, numero)
    if len(valores) > 0:
        if numero < valores[0]:
            valores.insert(0, numero)
        if numero > valores[0]:
            if numero > valores[0] and len(valores) == 1:
                valores.append(numero)
            if valores[0] < numero < valores[1]:
                valores.insert(1, numero)
            if numero > valores[1] and len(valores) <= 4:
                valores.append(numero)
            if valores[1] < numero < valores[2]:
                valores.insert(2, numero)
            if len(valores) > 2:
                if valores[1] < numero < valores[2]:
                    valores.insert(2, numero)
                if valores[2] < numero < valores[3]:
                    valores.insert(3, numero)

print(valores)
