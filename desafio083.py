lista1 = []
lista2 = []
expressão = input('Digite uma expressão matemática utilizando parênteses: ')
for simb in expressão:
    if simb == '(':
        lista1.append('(')
    if simb == ')':
        lista2.append(')')
if len(lista1) != len(lista2):
    print('Sua expressão está errada!')
else:
    print('Sua expressão está correta!')

#corrigido