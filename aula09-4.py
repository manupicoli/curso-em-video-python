frase = 'Curso em vídeo Python'
#divisão
print(frase.split())
#ele vai dividir onde tiver caracter de espaço dentro da str
#isso gera uma lista com cada uma das palavras sendo uma str própria
print('-'.join(frase.split()))

dividido = frase.split()
print(dividido[0])
print(dividido[2][3])