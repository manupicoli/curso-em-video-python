n = input('Insira uma frase qualquer: ').strip().upper()
print('A letra A aparece {} vezes na frase.'.format(n.count('A')))
print('A primeira letra A apareceu na posição {}'.format(n.find('A')+1))
print('A última letra A apareceu na posição {}'.format(n.rfind('A')+1))
#rfid para começar a procurar pelo lado direito