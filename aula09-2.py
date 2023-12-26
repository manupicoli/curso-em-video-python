frase = 'Curso em vídeo Python'
#análise
print(len(frase))
#comprimento da frase: len = length
print(frase.count('o'))
#contar quantos 'o' têm na frase
print(frase.count('o', 0, 14))
#contando e já fazendo fatiamento com o 0, 14
print(frase.find('deo'))
#vai mostrar onde que começa os caracteres indicados
print(frase.find('android'))
#quando a string não existe, o valor retornado vai ser -1
print('Curso' in frase)
#existe? vai retornar True ou False
